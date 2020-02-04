from collections import defaultdict

from branch_build import RepoAndBuilds, RepoInfo, AppveyorConfig, TravisConfig


class Builds:
    def __init__(self):
        self.builds = defaultdict(list)

    def __store_repo(self, build):
        self.builds[build.repo_info.user].append(build)

    def add_repo(self, user, project, branches, travis_build_info=TravisConfig(True),
                 appveyor_build_info=AppveyorConfig()):
        build = RepoAndBuilds(RepoInfo(user, project, branches), travis_build_info,
                              appveyor_build_info)
        self.__store_repo(build)
