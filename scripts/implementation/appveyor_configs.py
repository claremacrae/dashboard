from typing import Optional

from scripts.implementation import dashboard_utilities
from scripts.implementation.dashboard_utilities import hyperlinked_text
from scripts.implementation.github_repo_info import GitHubRepoInfo


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