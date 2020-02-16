from typing import List

from scripts import dashboard_utilities


class GitHubRepoInfo:
    """
    Class that represents a particular repository and all its active branches
    """

    def __init__(self, user: str, project: str, branches: List[str], type: str) -> None:
        self.user = user
        self.project = project
        self.branches = branches
        self.type = type

    def user_account_url(self) -> str:
        return f"https://github.com/{self.user}"

    def user_repos_link(self) -> str:
        text = self.user
        url = f"{self.user_account_url()}?tab=repositories"
        return dashboard_utilities.hyperlinked_text(text, url)

    def project_link(self) -> str:
        text = self.project
        url = f"{self.user_account_url()}/{self.project}/"
        return dashboard_utilities.hyperlinked_text(text, url)

    def network_link(self) -> str:
        text = 'network'
        url = f"{self.user_account_url()}/{self.project}/network"
        return dashboard_utilities.hyperlinked_text(text, url)

    def branch_link(self, branch: str) -> str:
        text = branch
        url = f"{self.user_account_url()}/{self.project}/commits/{branch}"
        return dashboard_utilities.hyperlinked_text(text, url)
