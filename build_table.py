class BuildTable:
    @staticmethod
    def write_header(stream):
        stream.write('<a id="top"></a>\n')
        stream.write('# dashboard\n')
        stream.write("A space to check build-statuses of projects I'm working on\n")
        stream.write('\n')
        BuildTable.write_table_title_rows(stream)

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

    def write_readme(self, all_builds):
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for user_names in all_builds.builds.keys():
                builds = all_builds.builds[user_names]
                user_name_row_written = False
                for build in builds:
                    if not user_name_row_written:
                        self.write_user_row(stream, build)
                        user_name_row_written = True
                    build.write_row(stream)