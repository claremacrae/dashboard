from scripts import dashboard_utilities

from scripts.ci_configs import AppveyorBuildConfig, GitHubBuildConfig, TravisBuildConfig
from typing import List


class RepoInfo:
    def __init__(self, user: str, project: str, branches: List[str], type: str) -> None:
        self.user = user
        self.project = project
        self.branches = branches
        self.type = type

    def user_link(self) -> str:
        text = self.user
        url = f"https://github.com/{self.user}?tab=repositories"
        return dashboard_utilities.hyperlinked_text(text, url)

    def project_link(self) -> str:
        text = self.project
        url = f"https://github.com/{self.user}/{self.project}/"
        return dashboard_utilities.hyperlinked_text(text, url)

    def network_link(self) -> str:
        text = 'network'
        url = f"https://github.com/{self.user}/{self.project}/network"
        return dashboard_utilities.hyperlinked_text(text, url)

    def branch_link(self, branch: str) -> str:
        text = branch
        url = f"https://github.com/{self.user}/{self.project}/commits/{branch}"
        return dashboard_utilities.hyperlinked_text(text, url)


class RepoAndBuilds:
    """
    Class that represents a particular repository and all its active branches and its CI builds
    """

    def __init__(self, repo_info: RepoInfo, travis_build_info: TravisBuildConfig,
                 appveyor_build_info: AppveyorBuildConfig, github_build_info: GitHubBuildConfig) -> None:
        self.repo_info = repo_info
        self.travis_build_info = travis_build_info
        self.appveyor_build_info = appveyor_build_info
        self.github_build_info = github_build_info
