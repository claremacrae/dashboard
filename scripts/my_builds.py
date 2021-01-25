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


def add_official_approval_test_repos_cpp(builds: AllRepos) -> None:
    repo = 'ApprovalTests.cpp'
    gh_workflows = ['build', 'python-tests']
    builds.add_source_repo('approvals', repo, ['master'], AppveyorBuildConfig('lf3i76ije89oihi5', 'isidore'),
                           GitHubBuildConfig(gh_workflows))
    builds.add_forked_repo('claremacrae', repo, ['master'], AppveyorBuildConfig('37smtsp3a694okv8'),
                           GitHubBuildConfig(gh_workflows))  # 'setup_sanitizers'

    repo = 'ApprovalTests.cpp.StarterProject'
    gh_workflows = ['build', 'build_vs']
    builds.add_source_repo('approvals', repo, ['master'], AppveyorBuildConfig('qx0546k6ii57919w', 'isidore'),
                           GitHubBuildConfig(gh_workflows))
    builds.add_forked_repo('claremacrae', repo, ['master'], AppveyorBuildConfig('ytjgybf5r9fviifm'),
                           GitHubBuildConfig(gh_workflows))

    repo = 'ApprovalTests.cpp.Qt'
    builds.add_source_repo('approvals', repo, ['master'], AppveyorBuildConfig('pf8et0nk1mdajskf', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], AppveyorBuildConfig('g60qbttap7m5nul2'))

    repo = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_source_repo('approvals', repo, ['master'], AppveyorBuildConfig('tpitsul9axlv93uk', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], AppveyorBuildConfig('xe2iwuto0sc342a7'))


def add_official_approval_test_repos_python(builds: AllRepos) -> None:
    repo = 'ApprovalTests.Python'
    git_hub_build_config = GitHubBuildConfig(['Test', 'on-push-do-doco', 'Upload Python Package'], False)
    builds.add_source_repo('approvals', repo, ['master'], None, git_hub_build_config)


def add_my_experimental_approvals_repos(builds: AllRepos) -> None:
    builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.CMakeSamples', ['main'], None)
    builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Demos', ['main'], None)
    builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Nursery', ['main'], None)

    repos = [
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo in repos:
        builds.add_source_repo('claremacrae', repo, ['main'], None, None)


def add_my_random_repos(builds: AllRepos) -> None:
    # clone of other people's work - using CMake's FetchContent:
    # builds.add_builds('claremacrae', 'approval-tests-setup', ['master'])
    builds.add_source_repo('claremacrae', 'ci_playground', ['trunk'], AppveyorBuildConfig('cbksrgvypq5vksy2'))
    builds.add_source_repo('claremacrae', 'cpp_snippets', ['main'], AppveyorBuildConfig('hqf8xh615dyp3u4l'), None)


def add_catch_repos(builds):
    repo = 'Catch2'
    builds.add_source_repo('catchorg', repo, ['master'])
    builds.add_forked_repo('claremacrae', repo, ['master'], AppveyorBuildConfig('8m77qos96rmcn6jg'))


def add_boost_ut_repos(builds):
    repo = 'ut'
    builds.add_source_repo('boost-experimental', repo, ['master'])
    builds.add_forked_repo('claremacrae', repo, ['master', 'clare_learning'], AppveyorBuildConfig('ab4jv9x8kveev0n4'))


def add_doctest_repos(builds: AllRepos) -> None:
    repo = 'doctest'
    builds.add_source_repo('onqtam', repo, ['master', 'dev'], github_build_info=GitHubBuildConfig(['CI']))
    builds.add_forked_repo('claremacrae', repo, ['master', 'dev'], AppveyorBuildConfig('y3ylbpuv79souy6e'),
                           GitHubBuildConfig(['CI']))
