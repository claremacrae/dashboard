from collections import defaultdict
from typing import DefaultDict, List

from scripts.ci_configs import TravisBuildConfig, AppveyorBuildConfig, GitHubBuildConfig, RepoAndBuilds
from scripts.github_repo_info import GitHubRepoInfo


class AllRepos:
    def __init__(self) -> None:
        self.builds: DefaultDict[str, list] = defaultdict(list)

    def builds_for_user_and_type(self, repo_type: str, user_name: str) -> List[RepoAndBuilds]:
        builds = self.builds[user_name]
        return [build for build in builds if build.repo_info.type == repo_type]

    def __store_repo(self, repo):
        self.builds[repo.repo_info.user].append(repo)

    def add_source_repo(self, user: str, project: str, branches: List[str],
                        travis_build_info: TravisBuildConfig = TravisBuildConfig(True),
                        appveyor_build_info: AppveyorBuildConfig = AppveyorBuildConfig(),
                        github_build_info: GitHubBuildConfig = GitHubBuildConfig()) -> None:
        self.add_repo(appveyor_build_info, branches, project, travis_build_info, github_build_info, 'Source', user)

    def add_forked_repo(self, user: str, project: str, branches: List[str],
                        travis_build_info: TravisBuildConfig = TravisBuildConfig(True),
                        appveyor_build_info: AppveyorBuildConfig = AppveyorBuildConfig(),
                        github_build_info: GitHubBuildConfig = GitHubBuildConfig()) -> None:
        self.add_repo(appveyor_build_info, branches, project, travis_build_info, github_build_info, 'Fork', user)

    def add_repo(self, appveyor_build_info, branches, project, travis_build_info, github_build_info, repo_type, user):
        repo = RepoAndBuilds(GitHubRepoInfo(user, project, branches, repo_type), travis_build_info,
                             appveyor_build_info, github_build_info)
        self.__store_repo(repo)
