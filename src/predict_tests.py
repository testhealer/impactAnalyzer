import json
from src.extract_keywords import extract_keywords

def predict_affected_tests(pr_title, keyword_to_testcases_mapping):
    keywords = extract_keywords(pr_title)
    impacted_tests = set()

    for keyword in keywords:
        if keyword.lower() in keyword_to_testcases_mapping:
            impacted_tests.update(keyword_to_testcases_mapping[keyword.lower()])

    # If no specific keyword matches, consider all test cases
    if not impacted_tests:
        impacted_tests.update(keyword_to_testcases_mapping.get('all_tests', []))

    return list(impacted_tests)

if __name__ == "__main__":
    with open('data/historical_data.json') as f:
        historical_data = json.load(f)

    pr_title = "Resolve authentication problem in user login"  #for test, to be removed
    keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
    impacted_tests = predict_affected_tests(pr_title, keyword_to_testcases_mapping)
    print(impacted_tests)
