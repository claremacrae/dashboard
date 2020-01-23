from collections import defaultdict

from BranchBuild import BranchBuild


class Builds:
    def __init__(self):
        self.builds = defaultdict(list)

    def add_build(self, build):
        self.builds[build.user].append(build)

    def add_builds(self, user, project, branches, travis_com, appveyor_token=None, custom_appveyor_user=None):
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
            'project / branch',
            'network',
            '[Travis](https://travis-ci.com/claremacrae/)',
            '[Appveyor](https://ci.appveyor.com/projects)',
            'GitHub']
        stream.write(f"| {' | '.join(titles)} |\n")
        divider = '| '
        for _ in titles:
            divider += ' --- |'
        stream.write(f'{divider}\n')

    @staticmethod
    def write_user_row(stream, build):
        user_link_text = F'**Account: {build.user_link()}**'
        stream.write(f"| {user_link_text} |\n")

    def write_readme(self):
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for user_names in self.builds.keys():
                builds = self.builds[user_names]
                user_name_row_written = False
                for build in builds:
                    if not user_name_row_written:
                        self.write_user_row(stream, build)
                        user_name_row_written = True
                    build.write_row(stream)
