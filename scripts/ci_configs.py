from typing import Optional

from scripts import dashboard_utilities
from scripts.dashboard_utilities import hyperlinked_text
from scripts.github_repo_info import GitHubRepoInfo


class TravisBuildConfig:
    def __init__(self, travis_com: bool) -> None:
        # Travis info
        # see
        # https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if travis_com:
            self.travis_url_base_image = 'travis-ci.com'
            self.travis_url_base_target = self.travis_url_base_image
        else:
            self.travis_url_base_image = 'travis-ci.org'
            self.travis_url_base_target = 'travis-ci.org'

    @staticmethod
    def main_url() -> str:
        return 'https://travis-ci.com/dashboard'

    @staticmethod
    def column_title() -> str:
        return F'{hyperlinked_text("Travis", TravisBuildConfig.main_url())} / {hyperlinked_text("Links", "/links/travis.md")}'

    def status(self, repo_info: GitHubRepoInfo, branch: str) -> str:
        # There is currently no way that I can see for linking to the current build on the chosen branch.
        # See this, for requests from others for this: https://github.com/travis-ci/travis-ci/issues/5024
        # For the workaround I'm currently using, see https://stackoverflow.com/a/32946454/104370
        # We now link to to all builds, allowing us to see all recent builds, in case the current build
        # has not yet completed.
        return dashboard_utilities.hyperlinked_image(
            "Build Status",
            f"https://{self.travis_url_base_image}/{repo_info.user}/{repo_info.project}.svg?branch={branch}",
            f"https://{self.travis_url_base_target}/{repo_info.user}/{repo_info.project}/builds")


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
    def __init__(self, workflow_name: str = 'build') -> None:
        self.workflow_name = workflow_name

    @staticmethod
    def column_title() -> str:
        return F'GitHub / {hyperlinked_text("Links", "/links/github_actions.md")}'

    def status(self, repo_info: GitHubRepoInfo, branch: str) -> str:
        user = repo_info.user
        project = repo_info.project
        result = ''
        result += dashboard_utilities.hyperlinked_image(
            "Build Status",
            f'https://github.com/{user}/{project}/workflows/{self.workflow_name}/badge.svg?branch={branch}',
            f'https://github.com/{user}/{project}/actions?query=branch%3A{branch}')
        return result

class RepoAndBuilds:
    """
    Class that represents a particular repository and all its active branches and its CI builds
    """

    def __init__(self, repo_info: GitHubRepoInfo, travis_build_info: TravisBuildConfig,
                 appveyor_build_info: AppveyorBuildConfig, github_build_info: GitHubBuildConfig) -> None:
        self.repo_info = repo_info
        self.travis_build_info = travis_build_info
        self.appveyor_build_info = appveyor_build_info
        self.github_build_info = github_build_info
