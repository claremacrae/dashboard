class Build:
    def __init__(self, user, project, branch):
        self.user = user
        self.project = project
        self.branch = branch

    def write_row(self, stream):
        line = f"| {self.user} | {self.project} | {self.branch} | [![Build Status](https://api.travis-ci.org/{self.user}/{self.project}.svg?branch={self.branch})](https://travis-ci.org/approvals/{self.project}) | [![Build status](https://ci.appveyor.com/api/projects/status/lf3i76ije89oihi5?svg=true)](https://ci.appveyor.com/project/isidore/approvaltests-cpp) |"
        stream.write(line + '\n')


class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, user, project, branch):
        build = Build(user, project, branch)
        self.builds.append(build)

    def add_builds(self, user, projects, branches):
        for branch in branches:
            for project in projects:
                self.add_build(user, project, branch)

    def write_header(self, stream):
        stream.write('# dashboard\n')
        stream.write("A space to check build-statuses of projects I'm working on\n")
        stream.write('\n')
        stream.write('| User | project | branch | [Travis](https://travis-ci.com/claremacrae/) | [Appveyor](https://ci.appveyor.com/projects) |\n')
        stream.write('| ------------- | ------------- | - | - | - |\n')

    def write_readme(self):
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for build in self.builds:
                build.write_row(stream)

def create_readme():
    builds = Builds()

    approvals_projects = ['ApprovalTests.cpp', 'ApprovalTests.cpp.StarterProject']
    builds.add_builds('approvals', approvals_projects, ['master'])
    builds.add_builds('claremacrae', approvals_projects, ['master', 'more_appveyor_builds'])
    builds.add_builds('claremacrae', ['ApprovalTests.cpp.Nursery'], ['master'])

    builds.write_readme()

if __name__ == '__main__':
    create_readme()
