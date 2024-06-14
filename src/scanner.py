from msrest.authentication import BasicAuthentication
from azure.devops.connection import Connection
from azure.devops.v7_0.git.git_client import GitClient
from azure.devops.v7_0.git.models import GitPullRequest, \
    GitPullRequestSearchCriteria


class PullRequestScanner:

    def __init__(
            self,
            organization: str,
            project: str,
            personal_access_token: str):
        if organization.startswith("http"):
            organization_url = organization
        else:
            organization_url = 'https://dev.azure.com/' + organization
        self.project = project
        # Create a connection to the org
        credentials = BasicAuthentication('', personal_access_token)
        self.connection = Connection(
            base_url=organization_url,
            creds=credentials)

    def get_pull_request_title(self, repository_id: str) -> str:
        git_client: GitClient = self.connection.clients_v7_0 \
            .get_git_client()
        criteria: GitPullRequestSearchCriteria = GitPullRequestSearchCriteria(
            status="active")
        pull_requests: list[GitPullRequest] = git_client.get_pull_requests(
            repository_id=repository_id,
            search_criteria=criteria,
            top=1)
        pull_request_titles = [x.title for x in pull_requests]
        return pull_request_titles[0]
