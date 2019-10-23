from Builds import Builds


def create_readme():
    builds = Builds()

    add_approval_tests_cpp(builds)
    add_approval_tests_cpp_starter_project(builds)
    add_approval_tests_cpp_nursery(builds)

    add_catch_projects(builds)
    add_my_miscellaneous(builds)

    builds.write_readme()

def add_approval_tests_cpp(builds):
    builds.add_builds('approvals', 'ApprovalTests.cpp', ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('claremacrae', 'ApprovalTests.cpp', ['master', 'setup_sanitizers'], True, '37smtsp3a694okv8')

def add_approval_tests_cpp_starter_project(builds):
    builds.add_builds('approvals', 'ApprovalTests.cpp.StarterProject', ['master'], False)
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.StarterProject', ['master'], True, 'mu8a5uib1ha7sx41')

def add_approval_tests_cpp_nursery(builds):
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.Nursery', ['master'], True, 'iqtnpa83t13os98v')


def add_my_miscellaneous(builds):
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, 'cbksrgvypq5vksy2')
    builds.add_builds('claremacrae', 'cpp_snippets', ['master'], True, 'hqf8xh615dyp3u4l')

def add_catch_projects(builds):
    builds.add_builds('catchorg', 'Catch2', ['master'], False)
    builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')


if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
