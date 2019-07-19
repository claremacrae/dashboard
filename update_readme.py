from BranchBuild import BranchBuild


class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, build):
        self.builds.append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token = None, custom_appveyor_user = None):
        for branch in branches:
            build = BranchBuild(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)
            self.add_build(build)

    def write_header(self, stream):
        stream.write('<a id="top"></a>\n')
        stream.write('# dashboard\n')
        stream.write("A space to check build-statuses of projects I'm working on\n")
        stream.write('\n')
        stream.write('| User | project | network | branch | [Travis](https://travis-ci.com/claremacrae/) | [Appveyor](https://ci.appveyor.com/projects) |\n')
        stream.write('| ------------- | ------------- - | -| - | - | - |\n')

    def write_readme(self):
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for build in self.builds:
                build.write_row(stream)

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
