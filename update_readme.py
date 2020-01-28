from build_table import BuildTable
from builds import Builds


def create_readme():
    builds = Builds()

    repo = 'ApprovalTests.cpp'
    builds.add_builds('approvals', repo, ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('claremacrae', repo, ['master'], True, '37smtsp3a694okv8')  # 'setup_sanitizers'

    repo1 = 'ApprovalTests.cpp.StarterProject'
    builds.add_builds('approvals', repo1, ['master'], False, 'qx0546k6ii57919w', 'isidore')
    builds.add_builds('claremacrae', repo1, ['master'], True, 'ytjgybf5r9fviifm')

    repo2 = 'ApprovalTests.cpp.Qt'
    builds.add_builds('approvals', repo2, ['master'], True, 'pf8et0nk1mdajskf', 'isidore')
    builds.add_builds('claremacrae', repo2, ['master'], True, 'g60qbttap7m5nul2')

    repo3 = 'ApprovalTests.cpp.Qt.StarterProject'
    builds.add_builds('approvals', repo3, ['master'], False, 'tpitsul9axlv93uk', 'isidore')
    builds.add_builds('claremacrae', repo3, ['master'], True, 'xe2iwuto0sc342a7')

    repo4 = 'ApprovalTests.cpp.Nursery'
    builds.add_builds('claremacrae', repo4, ['master'], True, 'iqtnpa83t13os98v')

    repos = [
        'ApprovalTests.cpp.Builds',
        'ApprovalTests.cpp.CMakeSamples',
        'ApprovalTests.cpp.Demos',
        # 'ApprovalTests.cpp.Scripts',
        'SuperBuildApprovalTests',
    ]
    for repo5 in repos:
        builds.add_builds('claremacrae', repo5, ['master'], True)

    # builds.add_builds('catchorg', 'Catch2', ['master'], False)
    # builds.add_builds('claremacrae', 'Catch2', ['master'], False, '8m77qos96rmcn6jg')

    builds.add_builds('claremacrae', 'approval-tests-setup', ['master'], True)
    builds.add_builds('claremacrae', 'ci_playground', ['trunk'], True, 'cbksrgvypq5vksy2')
    builds.add_builds('claremacrae', 'cpp_snippets', ['master'], True, 'hqf8xh615dyp3u4l')

    table = BuildTable()
    table.write_readme(builds)





if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
