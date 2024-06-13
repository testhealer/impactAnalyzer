from flask import Flask, render_template, request
import json
from src.create_mapping import create_keyword_to_testcase_mapping
from src.predict_tests import predict_affected_tests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        pr_title = request.form["pr_title"]
        with open('data/historical_data.json') as f:
            historical_data = json.load(f)

        keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
        prediction = predict_affected_tests(pr_title, keyword_to_testcases_mapping)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
