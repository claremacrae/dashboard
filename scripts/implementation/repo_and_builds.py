from typing import List, Union

from scripts.implementation.appveyor_configs import AppveyorBuildConfig
from scripts.implementation.github_configs import GitHubBuildConfig
from scripts.implementation.github_repo_info import GitHubRepoInfo


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