from typing import TextIO

from scripts.implementation.all_repos import AllRepos
from scripts.implementation.repo_and_builds import RepoAndBuilds


class BuildBadges:

    @staticmethod
    def write_row(stream: TextIO, branch_build: RepoAndBuilds) -> None:
        repo_info = branch_build.repo_info
        branch = repo_info.branches[0]

        number_of_badges = 0
        for build in branch_build.all_builds():
            if build:
                number_of_badges += 1
        if number_of_badges == 0:
            return

        stream.write(F'\n')
        stream.write(F'{repo_info.user}/{repo_info.project}\n')
        stream.write(F'\n')

        for build in branch_build.all_builds():
            if not build:
                continue
            link = build.status(repo_info, branch)
            wrapped_link = link.replace('  ', '\n')
            stream.write(F'{wrapped_link}\n')

    def write_badges(self, all_repos: AllRepos) -> None:
        with open('Badges.md', 'w') as stream:
            for user_name in all_repos.builds.keys():
                self.write_all_repos_for_user(all_repos, stream, user_name)

    def write_all_repos_for_user(self, all_repos: AllRepos, stream: TextIO, user_name: str) -> None:
        builds = all_repos.builds_for_user_and_type('Source', user_name)
        if not builds:
            return

        last_project_name = None
        for build in builds:
            project_name = build.repo_info.project
            if last_project_name == project_name:
                continue
            self.write_row(stream, build)
            last_project_name = project_name