import argparse
import sys
import json
from src.scanner import PullRequestScanner
from src.create_mapping import create_keyword_to_testcase_mapping
from src.predict_tests import predict_affected_tests

argument_parser = argparse.ArgumentParser(
    prog='python -m azure_devops_integration',
    description='Publishes messages for Azure DevOps builds \
        to Microsoft Teams')
argument_parser.add_argument(
    "-o", "--organization",
    action="store",
    help="The Azure DevOps organization name, for example ABB-BFA-ELDS, \
        or the URI of the TFS collection or Azure DevOps organization, \
        for example: https://dev.azure.com/ABB-BFA-ELDS")
argument_parser.add_argument(
    "-p", "--project",
    action="store",
    help="The Azure DevOps project name, for example TAS, \
        or the ID of the project, for example Azure DevOps \
        predefined variable System.TeamProjectId")
argument_parser.add_argument(
    "-t", "--pat",
    action="store",
    help="Azure DevOps personal access token with read to builds")
argument_parser.add_argument(
    "-r", "--repository_id",
    action="store",
    help="The repository id")
argument_parser.add_argument(
    "-pt", "--pull_request_title",
    action="store",
    help="Optional pull request title")

args = argument_parser.parse_args()

with open('data/historical_data.json') as f:
    historical_data = json.load(f)

keyword_to_testcases_mapping = create_keyword_to_testcase_mapping(
    historical_data)

if args.pull_request_title:
    pull_request_title = args.pull_request_title
elif args.organization and args.project and args.pat and args.repository_id:
    scanner = PullRequestScanner(
        args.organization,
        args.project,
        args.pat)
    pull_request_title = scanner.get_pull_request_title(args.repository_id)
else:
    argument_parser.print_help()
    sys.exit("No pull request title or Azure DevOps information provided")

impacted_tests = predict_affected_tests(
    pull_request_title,
    keyword_to_testcases_mapping)

print(f"Impacted tests for pull request \"{pull_request_title}\": {impacted_tests}")
