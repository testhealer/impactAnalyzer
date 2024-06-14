import json
from flask import Flask, render_template, request
from src.create_mapping import create_keyword_to_testcase_mapping
from src.predict_tests import predict_affected_tests
from src.scanner import PullRequestScanner
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
app.config.from_prefixed_env()


# Mock function to get the latest PR name from Azure
def get_latest_pr_name():
    # Here, you would normally fetch the PR name from Azure.
    # This is a placeholder for demonstration purposes.
    # return "Fix critical bug in payment processing"
    scanner = PullRequestScanner(
        app.config["ORGANIZATION"],
        app.config["PROJECT"],
        app.config["PERSONAL_ACCESS_TOKEN"])
    pull_request_title = scanner.get_pull_request_title(app.config["REPOSITORY_ID"])
    return pull_request_title


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    pr_title = None
    if request.method == "POST" and "pr_title" in request.form:
        pr_title = request.form["pr_title"]
    elif request.method == "POST":
        pr_title = get_latest_pr_name()
    if pr_title:
        with open('data/historical_data.json') as f:
            historical_data = json.load(f)
        keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
        prediction = predict_affected_tests(pr_title, keyword_to_testcases_mapping)
    return render_template("index.html", pr_title=pr_title, prediction=prediction)


@app.route("/latest_pr", methods=["POST"])
def latest_pr():
    pr_title = get_latest_pr_name()
    with open('data/historical_data.json') as f:
        historical_data = json.load(f)
    keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
    prediction = predict_affected_tests(pr_title, keyword_to_testcases_mapping)
    return render_template("index.html", pr_title=pr_title, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
