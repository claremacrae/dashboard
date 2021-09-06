from scripts.implementation.all_repos import AllRepos
from scripts.implementation.github_configs import GitHubBuildConfig


class CppApprovalTests:
    @staticmethod
    def add_all_repos(builds: AllRepos) -> None:
        # ApprovalTests.cpp
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp', ['master',
                                                                         ],
                                      None,
                                      GitHubBuildConfig(['build', 'cygwin', 'mingw', 'python-tests']))
        builds.add_forked_repo(repo,)  # 'setup_sanitizers'

        # ApprovalTests.cpp.StarterProject
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.StarterProject', ['master'],
                                      None,
                                      GitHubBuildConfig(['build', 'build_vs']))
        builds.add_forked_repo(repo)

        # ApprovalTests.cpp.Qt
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt', ['master'])
        builds.add_forked_repo(repo)

        # ApprovalTests.cpp.Qt.StarterProject
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt.StarterProject', ['master'])
        builds.add_forked_repo(repo)
