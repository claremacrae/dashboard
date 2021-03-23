from scripts.ClareRepos import ClareRepos
from scripts.CppApprovalTests import CppApprovalTests
from scripts.PythonApprovalTests import PythonApprovalTests
from scripts.implementation.all_repos import AllRepos
from scripts.implementation.ci_configs import AppveyorBuildConfig, GitHubBuildConfig


def add_all_repos(builds: AllRepos) -> None:
    CppApprovalTests.add_all_repos(builds)
    PythonApprovalTests.add_all_repos(builds)
    ClareRepos.add_all_my_repos(builds)

    # Other things I've forked - alphabetical by account name
    TestFrameworkRepos.add_all_repos(builds)


class TestFrameworkRepos:
    @staticmethod
    def add_all_repos(builds: AllRepos):
        # TestFrameworkRepos.add_boost_ut_repos(builds)
        # TestFrameworkRepos.add_catch_repos(builds)
        # TestFrameworkRepos.add_doctest_repos(builds)
        pass

    @staticmethod
    def add_catch_repos(builds: AllRepos):
        repo = builds.add_source_repo('catchorg', 'Catch2', ['master'])
        builds.add_forked_repo(repo, AppveyorBuildConfig('8m77qos96rmcn6jg'))

    @staticmethod
    def add_boost_ut_repos(builds: AllRepos):
        repo = builds.add_source_repo('boost-experimental', 'ut', ['master'])
        builds.add_forked_repo(repo, AppveyorBuildConfig('ab4jv9x8kveev0n4'), ['master', 'clare_learning'])

    @staticmethod
    def add_doctest_repos(builds: AllRepos) -> None:
        repo = builds.add_source_repo('onqtam', 'doctest', ['master', 'dev'],
                                      github_build_info=GitHubBuildConfig(['CI']))
        builds.add_forked_repo(repo, AppveyorBuildConfig('y3ylbpuv79souy6e'), ['master', 'dev'])
