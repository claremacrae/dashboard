from scripts.implementation.all_repos import AllRepos
from scripts.implementation.github_configs import GitHubBuildConfig
from scripts.implementation.appveyor_configs import AppveyorBuildConfig


class CppApprovalTests:
    @staticmethod
    def add_all_repos(builds: AllRepos) -> None:
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp', ['master'],
                                      AppveyorBuildConfig('lf3i76ije89oihi5', 'isidore'),
                                      GitHubBuildConfig(['build', 'python-tests']))
        builds.add_forked_repo(repo, AppveyorBuildConfig('37smtsp3a694okv8'))  # 'setup_sanitizers'

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.StarterProject', ['master'],
                                      None,
                                      GitHubBuildConfig(['build', 'build_vs']))
        builds.add_forked_repo(repo, AppveyorBuildConfig('ytjgybf5r9fviifm'))

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt', ['master'],
                                      AppveyorBuildConfig('pf8et0nk1mdajskf', 'isidore'))
        builds.add_forked_repo(repo, AppveyorBuildConfig('g60qbttap7m5nul2'))

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt.StarterProject', ['master'],
                                      AppveyorBuildConfig('tpitsul9axlv93uk', 'isidore'))
        builds.add_forked_repo(repo, AppveyorBuildConfig('xe2iwuto0sc342a7'))