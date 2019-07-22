from Builds import Builds


def create_readme():
    builds = Builds()

    add_approvals_builds(builds)
    add_ci_playground(builds)
    add_my_approvals_projects(builds)

    builds.write_readme()


def add_my_approvals_projects(builds):
    my_branches = ['master']
    builds.add_builds('claremacrae', 'ApprovalTests.cpp', my_branches, True, '37smtsp3a694okv8')
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.StarterProject', my_branches, True, 'mu8a5uib1ha7sx41')
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.Nursery', ['master'], True, 'iqtnpa83t13os98v')


def add_ci_playground(builds):
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, 'cbksrgvypq5vksy2')


def add_approvals_builds(builds):
    builds.add_builds('approvals', 'ApprovalTests.cpp', ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('approvals', 'ApprovalTests.cpp.StarterProject', ['master'], False)


if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
