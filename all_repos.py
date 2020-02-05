from collections import defaultdict

from repo_and_builds import RepoAndBuilds, RepoInfo, AppveyorConfig, TravisConfig


class AllRepos:
    def __init__(self):
        self.builds = defaultdict(list)

    def __store_repo(self, repo):
        self.builds[repo.repo_info.user].append(repo)

    def add_source_repo(self, user, project, branches, travis_build_info=TravisConfig(True),
                        appveyor_build_info=AppveyorConfig()):
        type = 'Source'
        repo = RepoAndBuilds(RepoInfo(user, project, branches, type), travis_build_info,
                             appveyor_build_info)
        self.__store_repo(repo)
