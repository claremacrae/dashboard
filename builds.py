from collections import defaultdict

from branch_build import BranchBuild, RepoInfo, AppveyorConfig


class Builds:
    def __init__(self):
        self.builds = defaultdict(list)

    def add_build(self, build):
        self.builds[build.repo_info.user].append(build)

    def add_builds(self, user, project, branches, travis_build_info, appveyor_build_info = AppveyorConfig()):
        for branch in branches:
            build = BranchBuild(RepoInfo(user, project, branch), travis_build_info,
                                appveyor_build_info)
            self.add_build(build)
