class BuildBadges:

    @staticmethod
    def write_row(stream, branch_build):
        branch = branch_build.repo_info.branches[0]
        links = [
            branch_build.travis_build_info.status(branch_build.repo_info, branch),
            branch_build.appveyor_build_info.status(branch_build.repo_info, branch),
            branch_build.github_build_info.status(branch_build.repo_info, branch),
        ]
        stream.write(F'\n')
        stream.write(F'{branch_build.repo_info.user}/{branch_build.repo_info.project}\n')
        stream.write(F'\n')
        for link in links:
            stream.write(F'{link} \n')

    def write_badges(self, all_builds):
        with open('Badges.md', 'w') as stream:
            for user_names in all_builds.builds.keys():
                builds = all_builds.builds[user_names]
                for build in builds:
                    self.write_row(stream, build)
