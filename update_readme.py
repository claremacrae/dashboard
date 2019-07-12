class Build:
    def __init__(self, user, project, branch, travis_com):
        self.user = user
        self.project = project
        self.branch = branch
        self.travis_com = travis_com

    def write_row(self, stream):
        # TODO Add Appveyor link
        # TODO What if build does not exist yet?
        line = f"| {self.user} | {self.project} | {self.create_branch_link_markdown()} | {self.create_travis_status_markdown()} | |"
        stream.write(line + '\n')

    def create_branch_link_markdown(self):
        return f"[{self.branch}](https://github.com/{self.user}/{self.project}/commits/{self.branch})"

    def create_travis_status_markdown(self):
        # see https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if self.travis_com:
            travis_url_base_image = 'travis-ci.com'
            travis_url_base_target = travis_url_base_image
        else:
            travis_url_base_image = 'api.travis-ci.org'
            travis_url_base_target = 'travis-ci.org'
        travis_status_markdown = \
            "[![Build Status](" + \
            f"https://{travis_url_base_image}/{self.user}/{self.project}.svg?branch={self.branch}" + \
            ")](" + \
            f"https://{travis_url_base_target}/{self.user}/{self.project}" + \
            ")"
        return travis_status_markdown


class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, user, project, branch, travis_com):
        build = Build(user, project, branch, travis_com)
        self.builds.append(build)

    def add_builds(self, user, projects, branches, travis_com):
        for branch in branches:
            for project in projects:
                self.add_build(user, project, branch, travis_com)

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
    builds.add_builds('approvals', approvals_projects, ['master'], False)
    builds.add_builds('claremacrae', approvals_projects, ['master', 'more_travis_builds', 'more_appveyor_builds'], True)
    builds.add_builds('claremacrae', ['ApprovalTests.cpp.Nursery'], ['master'], True)

    builds.write_readme()

if __name__ == '__main__':
    create_readme()
