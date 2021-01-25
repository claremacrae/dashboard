from typing import Optional, List, Union

from scripts import dashboard_utilities
from scripts.dashboard_utilities import hyperlinked_text, encode_string
from scripts.github_repo_info import GitHubRepoInfo


class AppveyorBuildConfig:
    def __init__(self, appveyor_token: Optional[str] = None, custom_appveyor_user: Optional[str] = None) -> None:
        self.appveyor_token = appveyor_token
        self.custom_appveyor_user = custom_appveyor_user

    @staticmethod
    def main_url() -> str:
        return 'https://ci.appveyor.com/projects'

    @staticmethod
    def column_title() -> str:
        return F'{hyperlinked_text("Appveyor", AppveyorBuildConfig.main_url())} / {hyperlinked_text("Links", "/links/appveyor.md")}'

    def status(self, repo_info: GitHubRepoInfo, branch: str) -> str:
        if not self.appveyor_token:
            return '` `'

        appveyor_project = repo_info.project.lower().replace('.', '-').replace('_', '-')
        if self.custom_appveyor_user:
            appveyor_user = self.custom_appveyor_user
        else:
            appveyor_user = repo_info.user

        return dashboard_utilities.hyperlinked_image(
            "Build status",
            f"https://ci.appveyor.com/api/projects/status/{self.appveyor_token}/branch/{branch}?svg=true",
            f"https://ci.appveyor.com/project/{appveyor_user}/{appveyor_project}/branch/{branch}")


class GitHubBuildConfig:
    def __init__(self, workflow_names: List[str] = ['build']) -> None:
        self.workflow_names = workflow_names

    @staticmethod
    def column_title() -> str:
        return F'GitHub / {hyperlinked_text("Links", "/links/github_actions.md")}'

    def status(self, repo_info: GitHubRepoInfo, branch: str) -> str:
        user = repo_info.user
        project = repo_info.project
        result = ''
        for workflow_name in self.workflow_names:
            if len(result) > 0:
                result += "  "
            encoded_workflow_name = encode_string(workflow_name)
            result += dashboard_utilities.hyperlinked_image(
                "Build Status",
                f'https://github.com/{user}/{project}/workflows/{encoded_workflow_name}/badge.svg?branch={branch}',
                f'https://github.com/{user}/{project}/actions?query=branch%3A{branch}+workflow%3A{encoded_workflow_name}')
        return result

class RepoAndBuilds:
    """
    Class that represents a particular repository and all its active branches and its CI builds
    """

    def __init__(self, repo_info: GitHubRepoInfo, appveyor_build_info: AppveyorBuildConfig,
                 github_build_info: GitHubBuildConfig) -> None:
        self.repo_info = repo_info
        self.appveyor_build_info = appveyor_build_info
        self.github_build_info = github_build_info

    def all_builds(self) -> List[Union[AppveyorBuildConfig, GitHubBuildConfig]]:
        return [
            self.appveyor_build_info,
            self.github_build_info,
        ]
