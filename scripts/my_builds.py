from scripts.repo_and_builds import AppveyorConfig, TravisConfig


def add_all_repos(builds):
    add_official_approval_test_repos(builds)

    add_my_experimental_approvals_repos(builds)

    # builds.add_builds('catchorg', 'Catch2', ['master'], False)
    # builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')

    add_my_random_repos(builds)

    add_boost_ut_repos(builds)


def add_official_approval_test_repos(builds):
    repo = 'ApprovalTests.cpp'
    builds.add_source_repo('approvals', repo, ['master'], TravisConfig(False),
                           AppveyorConfig('lf3i76ije89oihi5', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], TravisConfig(True),
                           AppveyorConfig('37smtsp3a694okv8'))  # 'setup_sanitizers'

    repo = 'ApprovalTests.cpp.StarterProject'
    builds.add_source_repo('approvals', repo, ['master'], TravisConfig(False),
                           AppveyorConfig('qx0546k6ii57919w', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], TravisConfig(True), AppveyorConfig('ytjgybf5r9fviifm'))

    repo = 'ApprovalTests.cpp.Qt'
    builds.add_source_repo('approvals', repo, ['master'], TravisConfig(True),
                           AppveyorConfig('pf8et0nk1mdajskf', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], TravisConfig(True), AppveyorConfig('g60qbttap7m5nul2'))

    repo = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_source_repo('approvals', repo, ['master'], TravisConfig(False),
                           AppveyorConfig('tpitsul9axlv93uk', 'isidore'))
    builds.add_forked_repo('claremacrae', repo, ['master'], TravisConfig(True), AppveyorConfig('xe2iwuto0sc342a7'))


def add_my_experimental_approvals_repos(builds):
    repos = [
        'ApprovalTests.cpp.CMakeSamples',
        'ApprovalTests.cpp.Demos',
    ]
    for repo in repos:
        builds.add_source_repo('claremacrae', repo, ['master'])

    builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Nursery', ['master'], TravisConfig(True),
                           AppveyorConfig('iqtnpa83t13os98v'))

    repos = [
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo in repos:
        builds.add_source_repo('claremacrae', repo, ['master'])


def add_my_random_repos(builds):
    # clone of other people's work - using CMake's FetchContent:
    # builds.add_builds('claremacrae', 'approval-tests-setup', ['master'])
    builds.add_source_repo('claremacrae', 'ci_playground', ['trunk'], TravisConfig(True),
                           AppveyorConfig('cbksrgvypq5vksy2'))
    builds.add_source_repo('claremacrae', 'cpp_snippets', ['master'], TravisConfig(True),
                           AppveyorConfig('hqf8xh615dyp3u4l'))


def add_boost_ut_repos(builds):
    repo = 'ut'
    builds.add_source_repo('boost-experimental', repo, ['master'], TravisConfig(False))
    builds.add_forked_repo('claremacrae', repo, ['master', 'clare_learning'], TravisConfig(True),
                           AppveyorConfig('ab4jv9x8kveev0n4'))
