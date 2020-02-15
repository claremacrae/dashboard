from collections import defaultdict

from scripts.repo_and_builds import RepoAndBuilds, RepoInfo, AppveyorConfig, TravisConfig, GitHubBuildConfig


class AllRepos:
    def __init__(self):
        self.builds = defaultdict(list)

    def __store_repo(self, repo):
        self.builds[repo.repo_info.user].append(repo)

    def add_source_repo(self, user, project, branches, travis_build_info=TravisConfig(True),
                        appveyor_build_info=AppveyorConfig(), github_build_info=GitHubBuildConfig()):
        self.__add_repo(appveyor_build_info, branches, project, travis_build_info, github_build_info, 'Source', user)

    def add_forked_repo(self, user, project, branches, travis_build_info=TravisConfig(True),
                        appveyor_build_info=AppveyorConfig(), github_build_info=GitHubBuildConfig()):
        self.__add_repo(appveyor_build_info, branches, project, travis_build_info, github_build_info, 'Fork', user)

    def __add_repo(self, appveyor_build_info, branches, project, travis_build_info, github_build_info, type, user):
        repo = RepoAndBuilds(RepoInfo(user, project, branches, type), travis_build_info,
                             appveyor_build_info, github_build_info)
        self.__store_repo(repo)
