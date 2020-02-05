class BuildBadges:

    @staticmethod
    def write_row(stream, branch_build):
        repo_info = branch_build.repo_info
        branch = repo_info.branches[0]
        links = [
            branch_build.travis_build_info.status(repo_info, branch),
            branch_build.appveyor_build_info.status(repo_info, branch),
            branch_build.github_build_info.status(repo_info, branch),
        ]
        stream.write(F'\n')
        stream.write(F'{repo_info.user}/{repo_info.project}\n')
        stream.write(F'\n')
        for link in links:
            stream.write(F'{link} \n')

    def write_badges(self, all_repos):
        with open('Badges.md', 'w') as stream:
            for user_name in all_repos.builds.keys():
                self.write_all_repos_for_user(all_repos, stream, user_name)

    def write_all_repos_for_user(self, all_repos, stream, user_name):
        builds = all_repos.builds[user_name]
        for build in builds:
            self.write_row(stream, build)
