from branch_build import AppveyorConfig, TravisConfig


def add_all_builds(builds):
    add_official_approval_test_repos(builds)

    add_my_experimental_approvals_repos(builds)

    # builds.add_builds('catchorg', 'Catch2', ['master'], False)
    # builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')

    add_my_random_repos(builds)

    add_boost_ut_repos(builds)


def add_official_approval_test_repos(builds):
    repo = 'ApprovalTests.cpp'
    builds.add_builds('approvals', repo, ['master'], TravisConfig(False), AppveyorConfig('lf3i76ije89oihi5', 'isidore'))
    builds.add_builds('claremacrae', repo, ['master'], TravisConfig(True),
                      AppveyorConfig('37smtsp3a694okv8'))  # 'setup_sanitizers'

    repo1 = 'ApprovalTests.cpp.StarterProject'
    builds.add_builds('approvals', repo1, ['master'], TravisConfig(False), AppveyorConfig('qx0546k6ii57919w', 'isidore'))
    builds.add_builds('claremacrae', repo1, ['master'], TravisConfig(True), AppveyorConfig('ytjgybf5r9fviifm'))

    repo2 = 'ApprovalTests.cpp.Qt'
    builds.add_builds('approvals', repo2, ['master'], TravisConfig(True), AppveyorConfig('pf8et0nk1mdajskf', 'isidore'))
    builds.add_builds('claremacrae', repo2, ['master'], TravisConfig(True), AppveyorConfig('g60qbttap7m5nul2'))

    repo3 = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_builds('approvals', repo3, ['master'], TravisConfig(False), AppveyorConfig('tpitsul9axlv93uk', 'isidore'))
    builds.add_builds('claremacrae', repo3, ['master'], TravisConfig(True), AppveyorConfig('xe2iwuto0sc342a7'))


def add_my_experimental_approvals_repos(builds):
    repo4 = 'ApprovalTests.cpp.Nursery'
    builds.add_builds('claremacrae', repo4, ['master'], TravisConfig(True), AppveyorConfig('iqtnpa83t13os98v'))
    repos = [
        'ApprovalTests.cpp.Builds',
        'ApprovalTests.cpp.CMakeSamples',
        'ApprovalTests.cpp.Demos',
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo5 in repos:
        builds.add_builds('claremacrae', repo5, ['master'], TravisConfig(True), AppveyorConfig())


def add_my_random_repos(builds):
    builds.add_builds('claremacrae', 'approval-tests-setup', ['master'], TravisConfig(True), AppveyorConfig())
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], TravisConfig(True), AppveyorConfig('cbksrgvypq5vksy2'))
    builds.add_builds('claremacrae', 'cpp_snippets', ['master'], TravisConfig(True), AppveyorConfig('hqf8xh615dyp3u4l'))


def add_boost_ut_repos(builds):
    repo = 'ut'
    builds.add_builds('boost-experimental', repo, ['master'], TravisConfig(False), AppveyorConfig())
    builds.add_builds('claremacrae', repo, ['master', 'clare_learning'], TravisConfig(True), AppveyorConfig('ab4jv9x8kveev0n4'))
