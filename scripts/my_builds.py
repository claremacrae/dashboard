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


class ClareRepos:
    @staticmethod
    def add_all_my_repos(builds: AllRepos):
        # ClareRepos.add_clion_webinar(builds)
        ClareRepos.add_misc_approvals(builds)
        ClareRepos.add_my_random_repos(builds)

    @staticmethod
    def add_clion_webinar(builds):
        builds.add_source_repo('claremacrae', 'commandline-videostore-cpp',
                               ['starting-point', 'complete-run', 'webinar'],
                               github_build_info=GitHubBuildConfig(['build', 'on-push-do-doco']),
                               language="Webinar")

    @staticmethod
    def add_misc_approvals(builds):
        misc = 'Miscellaneous'
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.CMakeSamples', ['main'], language=misc)
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Demos', ['main'], language=misc)
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Nursery', ['main'], language=misc)
        repos = [
            # 'ApprovalTests.cpp.Scripts',
            'SuperBuildApprovalTests',
        ]
        for repo in repos:
            builds.add_source_repo('claremacrae', repo, ['main'], None, None, language=misc)

    @staticmethod
    def add_my_random_repos(builds: AllRepos) -> None:
        language = 'Miscellaneous'
        # clone of other people's work - using CMake's FetchContent:
        # builds.add_builds('claremacrae', 'approval-tests-setup', ['master'])
        builds.add_source_repo('claremacrae', 'ci_playground', ['trunk'], AppveyorBuildConfig('cbksrgvypq5vksy2'),
                               language=language)
        builds.add_source_repo('claremacrae', 'cpp_snippets', ['main'], AppveyorBuildConfig('hqf8xh615dyp3u4l'),
                               None, language=language)


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
