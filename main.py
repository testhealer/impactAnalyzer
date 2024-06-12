import json
from src.create_mapping import create_keyword_to_testcase_mapping
from src.predict_tests import predict_affected_tests
from src.notify import send_notification


def main():
    with open('data/historical_data.json') as f:
        historical_data = json.load(f)

    keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)

    # New PR title example
    new_pr_title = "Fix login issue in user module"

    # Predict impacted tests
    impacted_tests = predict_affected_tests(new_pr_title, keyword_to_testcases_mapping)

    # Send notification
    send_notification('test_owner@example.com', new_pr_title, impacted_tests)


if __name__ == "__main__":
    main()
