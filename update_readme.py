from Builds import Builds


def create_readme():
    builds = Builds()

    builds.add_builds('approvals', 'ApprovalTests.cpp', ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('approvals', 'ApprovalTests.cpp.StarterProject', ['master'], False)

    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, 'cbksrgvypq5vksy2')

    my_branches = ['master']
    builds.add_builds('claremacrae', 'ApprovalTests.cpp', my_branches, True, '37smtsp3a694okv8')
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.StarterProject', my_branches, True, 'mu8a5uib1ha7sx41')

    builds.add_builds('claremacrae', 'ApprovalTests.cpp.Nursery', ['master'], True, 'iqtnpa83t13os98v')

    builds.write_readme()

if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
