class BranchBuild:
    """
    Class that generates a row in the dashboard to represent the current status of builds
    for a particular branch in a particular repo
    """
    def __init__(self, user, project, branch, travis_com, appveyor_token, custom_appveyor_user):
        self.user = user
        self.project = project
        self.branch = branch

        # Travis info
        # see https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if travis_com:
            self.travis_url_base_image = 'travis-ci.com'
            self.travis_url_base_target = self.travis_url_base_image
        else:
            self.travis_url_base_image = 'api.travis-ci.org'
            self.travis_url_base_target = 'travis-ci.org'

        # Appveyor info
        self.appveyor_token = appveyor_token
        self.appveyor_project = self.project.lower().replace('.', '-')
        if custom_appveyor_user:
            self.appveyor_user = custom_appveyor_user
        else:
            self.appveyor_user = self.user

    def write_row(self, stream):
        line = f"| {self.user_link()} | {self.project_link()} | {self.branch_link()} | {self.travis_status()} |{self.appveyor_status()} |"
        stream.write(line + '\n')

    def user_link(self):
        return f"[{self.user}](https://github.com/{self.user}/)"

    def project_link(self):
        return f"[{self.project}](https://github.com/{self.user}/{self.project}/)"

    def branch_link(self):
        return f"[{self.branch}](https://github.com/{self.user}/{self.project}/commits/{self.branch})"

    def hyperlinked_image(self, link_label, image_url, target_url):
        return f"[![{link_label}]({image_url})]({target_url})"

    def hyperlinked_text(self, link_label, target_url):
        return f"[{link_label}]({target_url})"

    def travis_status(self):
        # There is currently no way that I can see for linking to the current build on the chosen branch.
        # See this, for requests from others for this: https://github.com/travis-ci/travis-ci/issues/5024
        # For the workaround I'm currently using, see https://stackoverflow.com/a/32946454/104370
        # We now link to to all branches for which there are Travis builds, allowing the user to
        # click on the branch of interest, and see its latest build.
        return self.hyperlinked_image(
            "Build Status",
            f"https://{self.travis_url_base_image}/{self.user}/{self.project}.svg?branch={self.branch}",
            f"https://{self.travis_url_base_target}/{self.user}/{self.project}/branches")

    def appveyor_status(self):
        if not self.appveyor_token:
            return '&nbsp;'

        return self.hyperlinked_image(
            "Build status",
            f"https://ci.appveyor.com/api/projects/status/{self.appveyor_token}/branch/{self.branch}?svg=true",
            f"https://ci.appveyor.com/project/{self.appveyor_user}/{self.appveyor_project}/branch/{self.branch}")


class BuildHistory(BranchBuild):
    """
    Class that generates a row in the dashboard to represent links to the build history
    for all branches or builds in a particular repo
    """
    def __init__(self, user, project, travis_com, appveyor_token, custom_appveyor_user):
        super().__init__(user, project, None, travis_com, appveyor_token, custom_appveyor_user)

    def branch_link(self):
        return '&nbsp;'

    def travis_status(self):
        return self.hyperlinked_text(
            "branches",
            f"https://travis-ci.com/{self.user}/{self.project}/branches")

    def appveyor_status(self):
        if not self.appveyor_token:
            return '&nbsp;'

        return self.hyperlinked_text(
            "history",
            f"https://ci.appveyor.com/project/{self.appveyor_user}/{self.appveyor_project}/history")

class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, build):
        self.builds.append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token = None, custom_appveyor_user = None):
        # Add a first row, with links to all Travis branches and all Appveyor builds.
        # Currently disabled as it clutters up the table and distracts from the build status images
        # build = BuildHistory(user, project, travis_com, appveyor_token, custom_appveyor_user)
        # self.add_build(build)

        for branch in branches:
            build = BranchBuild(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)
            self.add_build(build)

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
