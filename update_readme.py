from build_table import BuildTable
from builds import Builds


def create_readme():
    builds = Builds()

    add_approval_tests_cpp(builds)
    add_approval_tests_cpp_starter_project(builds)
    add_approval_tests_cpp_qt(builds)
    add_approval_tests_cpp_qt_starter_project(builds)
    add_approval_tests_cpp_nursery(builds)
    add_approval_tests_cpp_builds(builds)

    # add_catch_projects(builds)
    add_my_miscellaneous(builds)

    table = BuildTable()
    table.write_readme(builds)


def add_approval_tests_cpp(builds):
    repo = 'ApprovalTests.cpp'
    builds.add_builds('approvals', repo, ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('claremacrae', repo, ['master'], True, '37smtsp3a694okv8')  # 'setup_sanitizers'


def add_approval_tests_cpp_starter_project(builds):
    repo = 'ApprovalTests.cpp.StarterProject'
    builds.add_builds('approvals', repo, ['master'], False)
    builds.add_builds('claremacrae', repo, ['master'], True)


def add_approval_tests_cpp_qt(builds):
    repo = 'ApprovalTests.cpp.Qt'
    builds.add_builds('approvals', repo, ['master'], True)
    builds.add_builds('claremacrae', repo, ['master'], True, 'g60qbttap7m5nul2')


def add_approval_tests_cpp_qt_starter_project(builds):
    repo = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_builds('approvals', repo, ['master'], False)
    builds.add_builds('claremacrae', repo, ['master'], True, 'g60qbttap7m5nul2')


def add_approval_tests_cpp_nursery(builds):
    repo = 'ApprovalTests.cpp.Nursery'
    builds.add_builds('claremacrae', repo, ['master'], True, 'iqtnpa83t13os98v')


def add_approval_tests_cpp_builds(builds):
    repos = [
        'ApprovalTests.cpp.Builds',
        'ApprovalTests.cpp.CMakeSamples',
        'ApprovalTests.cpp.Demos',
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo in repos:
        builds.add_builds('claremacrae', repo, ['master'], True)


def add_my_miscellaneous(builds):
    builds.add_builds('claremacrae', 'approval-tests-setup', ['master'], True)
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, 'cbksrgvypq5vksy2')
    builds.add_builds('claremacrae', 'cpp_snippets', ['master'], True, 'hqf8xh615dyp3u4l')


# def add_catch_projects(builds):
#     builds.add_builds('catchorg', 'Catch2', ['master'], False)
#     builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')
#     pass


if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
