from scripts.implementation.all_repos import AllRepos
from scripts.implementation.github_configs import GitHubBuildConfig
from scripts.implementation.appveyor_configs import AppveyorBuildConfig


class ClareRepos:
    @staticmethod
    def add_all_my_repos(builds: AllRepos) -> None:
        # ClareRepos.add_clion_webinar(builds)
        ClareRepos.add_misc_approvals(builds)
        ClareRepos.add_my_random_repos(builds)

    @staticmethod
    def add_clion_webinar(builds: AllRepos) -> None:
        branches_and_workflows = [
            [
                ['starting-point',],
                ['build', 'on-push-do-doco']
            ],
            [
                ['complete-run', 'webinar'],
                ['build']
            ],
        ]
        for branches, workflows in branches_and_workflows:
            builds.add_source_repo('claremacrae', 'commandline-videostore-cpp',
                                   branches,
                                   github_build_info=GitHubBuildConfig(workflows),
                                   language="Webinar")

    @staticmethod
    def add_misc_approvals(builds: AllRepos) -> None:
        misc = 'Miscellaneous'
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.CMakeSamples', ['main'], language=misc)
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Demos', ['main'], language=misc)
        builds.add_source_repo('claremacrae', 'ApprovalTests.cpp.Nursery', ['main'], language=misc)

    @staticmethod
    def add_my_random_repos(builds: AllRepos) -> None:
        language = 'Miscellaneous'
        #
        builds.add_source_repo('claremacrae', 'sudoku-kata-cpp',
                               ['main', 'with-tests'],
                               None,
                               GitHubBuildConfig(['CMake']),
                               language='C++')
        # clone of other people's work - using CMake's FetchContent:
        # builds.add_builds('claremacrae', 'approval-tests-setup', ['master'])
        builds.add_source_repo('claremacrae', 'cpp_snippets', ['main'], AppveyorBuildConfig('hqf8xh615dyp3u4l'),
                               None, language=language)
