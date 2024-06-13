import json
from src.create_mapping import create_keyword_to_testcase_mapping
from src.predict_tests import predict_affected_tests
from src.notify import send_notification

def main(pr_title):
    with open('data/historical_data.json') as f:
        historical_data = json.load(f)

    keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
    impacted_tests = predict_affected_tests(pr_title, keyword_to_testcases_mapping)
    print(impacted_tests)
    #send_notification(impacted_tests)

if __name__ == "__main__":
    pr_title = "Move new event variables to audit data"
    main(pr_title)
