from extract_keywords import extract_keywords

def predict_affected_tests(pr_title, keyword_to_testcases_mapping):
    keywords = extract_keywords(pr_title)
    impacted_tests = set()

    for keyword in keywords:
        if keyword.lower() in keyword_to_testcases_mapping:
            impacted_tests.update(keyword_to_testcases_mapping[keyword.lower()])

    return list(impacted_tests)
