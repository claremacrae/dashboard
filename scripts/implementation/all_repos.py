from collections import defaultdict
from typing import DefaultDict, List, Union

from scripts.implementation.ci_configs import AppveyorBuildConfig, GitHubBuildConfig, RepoAndBuilds
from scripts.github_repo_info import GitHubRepoInfo


class AllRepos:
    def __init__(self) -> None:
        self.builds: DefaultDict[str, list] = defaultdict(list)

    def builds_for_user_and_type(self, repo_type: str, user_name: str) -> List[RepoAndBuilds]:
        builds = self.builds[user_name]
        return [build for build in builds if build.repo_info.repo_type == repo_type]

    def __store_repo(self, repo):
        self.builds[repo.repo_info.user].append(repo)

    def add_source_repo(self, user: str, project: str, branches: Union[List[str], None],
                        appveyor_build_info: Union[AppveyorBuildConfig, None] = None,
                        github_build_info: Union[GitHubBuildConfig, None] = GitHubBuildConfig(),
                        language='C++') -> RepoAndBuilds:
        return self.add_repo(appveyor_build_info, branches, project, github_build_info, 'Source', user, language)

    def add_forked_repo(self, parent_repo: RepoAndBuilds, appveyor_build_info: Union[AppveyorBuildConfig, None] = None,
                        branches: Union[List[str], None] = None,
                        github_build_info: Union[GitHubBuildConfig, None] = None) -> RepoAndBuilds:
        if not branches:
            branches = parent_repo.repo_info.branches
        # Do not copy appveyor_build_info from parent repo, as settings are never the same
        if not github_build_info:
            github_build_info = parent_repo.github_build_info
        return self.add_repo(appveyor_build_info, branches, parent_repo.repo_info.project, github_build_info, 'Fork',
                             'claremacrae',
                             parent_repo.repo_info.language)

    def add_repo(self, appveyor_build_info: Union[AppveyorBuildConfig, None], branches: List[str], project: str,
                 github_build_info: Union[GitHubBuildConfig, None], repo_type: str, user: str,
                 language) -> RepoAndBuilds:
        repo = RepoAndBuilds(GitHubRepoInfo(user, project, branches, repo_type, language), appveyor_build_info,
                             github_build_info)
        self.__store_repo(repo)
        return repo
