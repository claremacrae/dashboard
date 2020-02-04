from collections import defaultdict

from branch_build import RepoAndBuilds, RepoInfo, AppveyorConfig, TravisConfig


class Builds:
    def __init__(self):
        self.builds = defaultdict(list)

    def __store_repo(self, repo):
        self.builds[repo.repo_info.user].append(repo)

    def add_repo(self, user, project, branches, travis_build_info=TravisConfig(True),
                 appveyor_build_info=AppveyorConfig()):
        repo = RepoAndBuilds(RepoInfo(user, project, branches), travis_build_info,
                              appveyor_build_info)
        self.__store_repo(repo)
