class Build:
    def __init__(self, user, project, branch, travis_com, appveyor_token, custom_appveyor_user):
        self.user = user
        self.project = project
        self.branch = branch
        self.travis_com = travis_com
        self.appveyor_token = appveyor_token
        self.custom_appveyor_user = custom_appveyor_user

    def write_row(self, stream):
        # TODO Add Appveyor link
        # TODO What if build does not exist yet?
        line = f"| {self.user} | {self.project} | {self.branch_link_markdown()} | {self.travis_status_markdown()} |{self.create_appveyor_status_markdown()} |"
        stream.write(line + '\n')

    def branch_link_markdown(self):
        return f"[{self.branch}](https://github.com/{self.user}/{self.project}/commits/{self.branch})"

    def travis_status_markdown(self):
        # see https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if self.travis_com:
            travis_url_base_image = 'travis-ci.com'
            travis_url_base_target = travis_url_base_image
        else:
            travis_url_base_image = 'api.travis-ci.org'
            travis_url_base_target = 'travis-ci.org'

        # There is currently no way that I can see for including the branch name in the second URL here.
        # See this, for requests from others for this: https://github.com/travis-ci/travis-ci/issues/5024
        travis_status_markdown = \
            "[![Build Status](" + \
            f"https://{travis_url_base_image}/{self.user}/{self.project}.svg?branch={self.branch}" + \
            ")](" + \
            f"https://{travis_url_base_target}/{self.user}/{self.project}" + \
            ")"
        return travis_status_markdown

    def create_appveyor_status_markdown(self):
        if not self.appveyor_token:
            return ''

        project_locase = self.project.lower().replace('.', '-')
        if self.custom_appveyor_user:
            user = self.custom_appveyor_user
        else:
            user = self.user
        appveyor_markdown = \
            f"[![Build status]" + \
            f"(https://ci.appveyor.com/api/projects/status/{self.appveyor_token}/branch/{self.branch}?svg=true)" + \
            "](" + \
            f"https://ci.appveyor.com/project/{user}/{project_locase}/branch/{self.branch}" + \
            ")"
        return appveyor_markdown

class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, user, project, branch, travis_com, appveyor_token, custom_appveyor_user):
        build = Build(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)
        self.builds.append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token = None, custom_appveyor_user = None):
        for branch in branches:
            self.add_build(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)

    def write_header(self, stream):
        stream.write('<a id="top"></a>\n')
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

    builds.add_builds('approvals', 'ApprovalTests.cpp', ['master'], False, 'lf3i76ije89oihi5', 'isidore')
    builds.add_builds('approvals', 'ApprovalTests.cpp.StarterProject', ['master'], False)

    my_branches = ['master', 'more_appveyor_builds']
    builds.add_builds('claremacrae', 'ApprovalTests.cpp', my_branches, True, '37smtsp3a694okv8')
    builds.add_builds('claremacrae', 'ApprovalTests.cpp.StarterProject', my_branches, True, 'mu8a5uib1ha7sx41')

    builds.add_builds('claremacrae', 'ApprovalTests.cpp.Nursery', ['master'], True, 'iqtnpa83t13os98v')

    builds.write_readme()

if __name__ == '__main__':
    create_readme()
