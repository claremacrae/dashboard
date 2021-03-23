from typing import TextIO

from scripts.implementation.all_repos import AllRepos
from scripts.implementation.ci_configs import AppveyorBuildConfig, RepoAndBuilds, GitHubBuildConfig


class BuildTable:
    @staticmethod
    def write_header(stream: TextIO) -> None:
        stream.write('<a id="top"></a>\n')
        stream.write('# dashboard\n')
        stream.write("A space to check build-statuses of projects I'm working on\n")
        stream.write('\n')
        BuildTable.write_table_title_rows(stream)

    @staticmethod
    def write_table_title_rows(stream: TextIO) -> None:
        titles = [
            'project / branch',
            'network',
            AppveyorBuildConfig.column_title(),
            GitHubBuildConfig.column_title()]
        stream.write(f"| {' | '.join(titles)} |\n")
        divider = '| '
        for _ in titles:
            divider += ' --- |'
        stream.write(f'{divider}\n')

    @staticmethod
    def write_user_row(stream: TextIO, build: RepoAndBuilds) -> None:
        user_link_text = F'**Account: {build.repo_info.user_repos_link()} - {build.repo_info.language} {build.repo_info.repo_type.lower()}s**'
        stream.write(f"| {user_link_text} |\n")

    @staticmethod
    def write_row(stream: TextIO, branch_build: RepoAndBuilds, branch: str) -> None:
        links = [
            F'{branch_build.repo_info.project_link()} / {branch_build.repo_info.branch_link(branch)}',
            branch_build.repo_info.network_link(),
        ]
        for build in branch_build.all_builds():
            links.append(BuildTable.get_status(build, branch_build, branch))
        line = ' | '.join(links)
        stream.write(F'| {line} |' + '\n')

    @staticmethod
    def get_status(build, branch_build, branch) -> str:
        if build:
            status = build.status(branch_build.repo_info, branch)
        else:
            status = ''
        return status

    def write_readme(self, all_repos: AllRepos) -> None:
        with open('README.md', 'w') as stream:
            self.write_header(stream)
            for user_name in all_repos.builds.keys():
                self.write_all_repos_for_user(all_repos, stream, user_name)

    def write_all_repos_for_user(self, all_repos: AllRepos, stream: TextIO, user_name: str) -> None:
        self.write_all_repos_of_type_for_user(all_repos, stream, 'Fork', user_name)
        self.write_all_repos_of_type_for_user(all_repos, stream, 'Source', user_name)

    def write_all_repos_of_type_for_user(self, all_repos: AllRepos, stream: TextIO, repo_type: str,
                                         user_name: str) -> None:
        builds = all_repos.builds_for_user_and_type(repo_type, user_name)
        if not builds:
            return
        first_build = builds[0]
        self.write_user_row(stream, first_build)
        last_language = first_build.repo_info.language
        for build in builds:
            language = build.repo_info.language
            if language != last_language:
                last_language = language
                self.write_user_row(stream, build)
            for branch in build.repo_info.branches:
                self.write_row(stream, build, branch)
