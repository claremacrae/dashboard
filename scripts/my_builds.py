from scripts.all_repos import AllRepos
from scripts.ci_configs import AppveyorBuildConfig, GitHubBuildConfig


def add_all_repos(builds: AllRepos) -> None:
    CppApprovalTests.add_official_approval_test_repos_cpp(builds)
    PythonApprovalTests.add_official_approval_test_repos_python(builds)
    add_my_experimental_approvals_repos(builds)
    add_my_random_repos(builds)

    # Other things I've forked - alphabetical by account name
    TestFrameworkRepos.add_all_repos(builds)


class CppApprovalTests:
    @staticmethod
    def add_official_approval_test_repos_cpp(builds: AllRepos) -> None:
        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp', ['master'],
                                      AppveyorBuildConfig('lf3i76ije89oihi5', 'isidore'),
                                      GitHubBuildConfig(['build', 'python-tests']))
        builds.add_forked_repo(repo, AppveyorBuildConfig('37smtsp3a694okv8'))  # 'setup_sanitizers'

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.StarterProject', ['master'],
                                      AppveyorBuildConfig('qx0546k6ii57919w', 'isidore'),
                                      GitHubBuildConfig(['build', 'build_vs']))
        builds.add_forked_repo(repo, AppveyorBuildConfig('ytjgybf5r9fviifm'))

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt', ['master'],
                                      AppveyorBuildConfig('pf8et0nk1mdajskf', 'isidore'))
        builds.add_forked_repo(repo, AppveyorBuildConfig('g60qbttap7m5nul2'))

        repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt.StarterProject', ['master'],
                                      AppveyorBuildConfig('tpitsul9axlv93uk', 'isidore'))
        builds.add_forked_repo(repo, AppveyorBuildConfig('xe2iwuto0sc342a7'))


class PythonApprovalTests:
    @staticmethod
    def add_official_approval_test_repos_python(builds: AllRepos) -> None:
        python = 'Python'
        default_workflows = ['Test', 'on-push-do-doco']  # We only show the publishing workflow in source repo
        parent_git_hub_build_config = GitHubBuildConfig(default_workflows + ['Upload Python Package'], False)
        repo = builds.add_source_repo('approvals', 'ApprovalTests.Python', ['master'], None,
                                      parent_git_hub_build_config,
                                      language=python)
        fork_git_hub_build_config = GitHubBuildConfig(default_workflows, False)
        builds.add_forked_repo(repo, github_build_info=fork_git_hub_build_config)

        repo = builds.add_source_repo('approvals', 'ApprovalTests.Python.PytestPlugin', ['master'], None,
                                      GitHubBuildConfig(['Test'], False), language=python)
        builds.add_forked_repo(repo)


def add_my_experimental_approvals_repos(builds: AllRepos) -> None:
    builds.add_source_repo('claremacrae', 'commandline-videostore-cpp', ['starting-point', 'complete-run', 'webinar'],
                           github_build_info=GitHubBuildConfig(['build', 'on-push-do-doco']),
                           language="Webinar")

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
