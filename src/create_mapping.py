import json
from collections import defaultdict
from extract_keywords import extract_keywords

def create_keyword_to_testcase_mapping(historical_data):
    keyword_to_testcases = defaultdict(set)

    for data in historical_data:
        keywords = extract_keywords(data['pr_title'])
        for keyword in keywords:
            for testcase in data['affected_tests']:
                keyword_to_testcases[keyword.lower()].add(testcase)

    return keyword_to_testcases

if __name__ == "__main__":
    with open('../data/historical_data.json') as f:
        historical_data = json.load(f)

    mapping = create_keyword_to_testcase_mapping(historical_data)
    print(mapping)
