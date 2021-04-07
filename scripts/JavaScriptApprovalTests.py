from scripts.implementation.all_repos import AllRepos
from scripts.implementation.github_configs import GitHubBuildConfig
from scripts.implementation.appveyor_configs import AppveyorBuildConfig


class JavaScriptApprovalTests:
    @staticmethod
    def add_all_repos(builds: AllRepos) -> None:
        JavaScriptApprovalTests.add_approvals_repos(builds)

    @staticmethod
    def add_approvals_repos(builds: AllRepos) -> None:
        language = 'JavaScript'

        repo = builds.add_source_repo('approvals', 'Approvals.NodeJS', ['master'],
                                      AppveyorBuildConfig('fwyi6sryl03h9em6', 'JasonJarrett'),
                                      None, language)
        repo = builds.add_source_repo('approvals', 'ApprovalTests.js.StarterProject', ['master'],
                                      None,
                                      None, language)
