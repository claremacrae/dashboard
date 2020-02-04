from collections import defaultdict

from branch_build import BranchBuild


class Builds:
    def __init__(self):
        self.builds = defaultdict(list)

    def add_build(self, build):
        self.builds[build.repo_info.user].append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token=None, custom_appveyor_user=None):
        for branch in branches:
            build = BranchBuild(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)
            self.add_build(build)
