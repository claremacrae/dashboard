from BranchBuild import BranchBuild


class Builds:
    def __init__(self):
        self.builds = []

    def add_build(self, build):
        self.builds.append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token = None, custom_appveyor_user = None, include_github_actions = False):
        for branch in branches:
            build = BranchBuild(user, project, branch, travis_com, appveyor_token, custom_appveyor_user)
            self.add_build(build)

    @staticmethod
    def write_header(stream):
        stream.write('<a id="top"></a>\n')
        stream.write('# dashboard\n')
        stream.write("A space to check build-statuses of projects I'm working on\n")
        stream.write('\n')
        Builds.write_table_title_rows(stream)

    @staticmethod
    def write_table_title_rows(stream):
        titles = [
            'User',
            'project',
            'network',
            'branch',
            '[Travis](https://travis-ci.com/claremacrae/)',
            '[Appveyor](https://ci.appveyor.com/projects)',
            'GitHub']
        stream.write(f"| {' | '.join(titles)} |\n")
        divider = '| '
        for title in titles:
            divider += ' --- |'
        stream.write(f'{divider}\n')

    def write_readme(self):
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for build in self.builds:
                build.write_row(stream)
