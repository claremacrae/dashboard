from scripts.all_repos import AllRepos
from scripts.ci_configs import AppveyorBuildConfig, GitHubBuildConfig


def add_all_repos(builds: AllRepos) -> None:
    add_official_approval_test_repos_cpp(builds)
    add_official_approval_test_repos_python(builds)
    add_my_experimental_approvals_repos(builds)
    add_my_random_repos(builds)

    # Other things I've forked - alphabetical by account name
    # add_boost_ut_repos(builds)
    # add_catch_repos(builds)
    # add_doctest_repos(builds)

# TODO Allow language to be supplied, and group README by language

def add_official_approval_test_repos_cpp(builds: AllRepos) -> None:
    gh_workflows = ['build', 'python-tests']
    repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp', ['master'],
                           AppveyorBuildConfig('lf3i76ije89oihi5', 'isidore'),
                           GitHubBuildConfig(gh_workflows))
    builds.add_forked_repo(repo, 'claremacrae', appveyor_build_info=AppveyorBuildConfig('37smtsp3a694okv8'))  # 'setup_sanitizers'

    gh_workflows = ['build', 'build_vs']
    repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.StarterProject', ['master'],
                           AppveyorBuildConfig('qx0546k6ii57919w', 'isidore'),
                           GitHubBuildConfig(gh_workflows))
    builds.add_forked_repo(repo, 'claremacrae', appveyor_build_info=AppveyorBuildConfig('ytjgybf5r9fviifm'))

    repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt', ['master'],
                           AppveyorBuildConfig('pf8et0nk1mdajskf', 'isidore'))
    builds.add_forked_repo(repo, 'claremacrae', appveyor_build_info=AppveyorBuildConfig('g60qbttap7m5nul2'))

    repo = builds.add_source_repo('approvals', 'ApprovalTests.cpp.Qt.StarterProject', ['master'],
                           AppveyorBuildConfig('tpitsul9axlv93uk', 'isidore'))
    builds.add_forked_repo(repo, 'claremacrae', appveyor_build_info=AppveyorBuildConfig('xe2iwuto0sc342a7'))


def add_official_approval_test_repos_python(builds: AllRepos) -> None:
    git_hub_build_config = GitHubBuildConfig(['Test', 'on-push-do-doco', 'Upload Python Package'], False)
    repo = builds.add_source_repo('approvals', 'ApprovalTests.Python', ['master'], None, git_hub_build_config)
    builds.add_forked_repo(repo, 'claremacrae')

    git_hub_build_config = GitHubBuildConfig(['Test'], False)
    repo = builds.add_source_repo('approvals', 'ApprovalTests.Python.PytestPlugin', ['master'], None, git_hub_build_config)
    builds.add_forked_repo(repo, 'claremacrae')


def add_my_experimental_approvals_repos(builds: AllRepos) -> None:
    repo = builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.CMakeSamples', ['main'], None)
    repo = builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Demos', ['main'], None)
    repo = builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Nursery', ['main'], None)

    repos = [
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo in repos:
        repo = builds.add_source_repo('claremacrae', repo, ['main'], None, None)


def add_my_random_repos(builds: AllRepos) -> None:
    # clone of other people's work - using CMake's FetchContent:
    # builds.add_builds('claremacrae', 'approval-tests-setup', ['master'])
    repo = builds.add_source_repo('claremacrae', 'ci_playground', ['trunk'], AppveyorBuildConfig('cbksrgvypq5vksy2'))
    repo = builds.add_source_repo('claremacrae', 'cpp_snippets', ['main'], AppveyorBuildConfig('hqf8xh615dyp3u4l'), None)


def add_catch_repos(builds):
    repo = builds.add_source_repo('catchorg', 'Catch2', ['master'])
    builds.add_forked_repo(repo, 'claremacrae', appveyor_build_info=AppveyorBuildConfig('8m77qos96rmcn6jg'))


def add_boost_ut_repos(builds):
    repo = builds.add_source_repo('boost-experimental', 'ut', ['master'])
    builds.add_forked_repo(repo, 'claremacrae', ['master', 'clare_learning'], AppveyorBuildConfig('ab4jv9x8kveev0n4'))


def add_doctest_repos(builds: AllRepos) -> None:
    repo = builds.add_source_repo('onqtam', 'doctest', ['master', 'dev'], github_build_info=GitHubBuildConfig(['CI']))
    builds.add_forked_repo(repo, 'claremacrae', ['master', 'dev'], AppveyorBuildConfig('y3ylbpuv79souy6e'))
