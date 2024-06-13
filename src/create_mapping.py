import json
from collections import defaultdict
from src.extract_keywords import extract_keywords

def create_keyword_to_testcase_mapping(historical_data):
    keyword_to_testcases = defaultdict(set)
    all_test_cases = historical_data['all_test_cases']

    for data in historical_data['historical_data']:
        keywords = extract_keywords(data['pr_title'])
        for keyword in keywords:
            for testcase in data['affected_tests']:
                keyword_to_testcases[keyword.lower()].add(testcase)

    # Include all test cases in the mapping
    for testcase in all_test_cases:
        keyword_to_testcases['all_tests'].add(testcase)

    return keyword_to_testcases

if __name__ == "__main__":
    with open('data/historical_data.json') as f:
        historical_data = json.load(f)

    keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(historical_data)
    print(keyword_to_testcases_mapping)
