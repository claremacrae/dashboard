from branch_build import AppveyorBuildInfo


def add_all_builds(builds):
    add_official_approval_test_repos(builds)

    add_my_experimental_approvals_repos(builds)

    # builds.add_builds('catchorg', 'Catch2', ['master'], False)
    # builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')

    add_my_random_repos(builds)

    add_boost_ut_repos(builds)


def add_official_approval_test_repos(builds):
    repo = 'ApprovalTests.cpp'
    builds.add_builds('approvals', repo, ['master'], False, AppveyorBuildInfo('lf3i76ije89oihi5', 'isidore'))
    builds.add_builds('claremacrae', repo, ['master'], True,
                      AppveyorBuildInfo('37smtsp3a694okv8'))  # 'setup_sanitizers'

    repo1 = 'ApprovalTests.cpp.StarterProject'
    builds.add_builds('approvals', repo1, ['master'], False, AppveyorBuildInfo('qx0546k6ii57919w', 'isidore'))
    builds.add_builds('claremacrae', repo1, ['master'], True, AppveyorBuildInfo('ytjgybf5r9fviifm'))

    repo2 = 'ApprovalTests.cpp.Qt'
    builds.add_builds('approvals', repo2, ['master'], True, AppveyorBuildInfo('pf8et0nk1mdajskf', 'isidore'))
    builds.add_builds('claremacrae', repo2, ['master'], True, AppveyorBuildInfo('g60qbttap7m5nul2'))

    repo3 = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_builds('approvals', repo3, ['master'], False, AppveyorBuildInfo('tpitsul9axlv93uk', 'isidore'))
    builds.add_builds('claremacrae', repo3, ['master'], True, AppveyorBuildInfo('xe2iwuto0sc342a7'))


def add_my_experimental_approvals_repos(builds):
    repo4 = 'ApprovalTests.cpp.Nursery'
    builds.add_builds('claremacrae', repo4, ['master'], True, AppveyorBuildInfo('iqtnpa83t13os98v'))
    repos = [
        'ApprovalTests.cpp.Builds',
        'ApprovalTests.cpp.CMakeSamples',
        'ApprovalTests.cpp.Demos',
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo5 in repos:
        builds.add_builds('claremacrae', repo5, ['master'], True, AppveyorBuildInfo())


def add_my_random_repos(builds):
    builds.add_builds('claremacrae', 'approval-tests-setup', ['master'], True, AppveyorBuildInfo())
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, AppveyorBuildInfo('cbksrgvypq5vksy2'))
    builds.add_builds('claremacrae', 'cpp_snippets', ['master'], True, AppveyorBuildInfo('hqf8xh615dyp3u4l'))


def add_boost_ut_repos(builds):
    repo = 'ut'
    builds.add_builds('boost-experimental', repo, ['master'], False, AppveyorBuildInfo())
    builds.add_builds('claremacrae', repo, ['master', 'clare_learning'], True, AppveyorBuildInfo('ab4jv9x8kveev0n4'))
