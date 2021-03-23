from scripts.implementation.all_repos import AllRepos
from scripts.implementation.ci_configs import GitHubBuildConfig


class JavaScriptApprovalTests:
    @staticmethod
    def add_all_repos(builds: AllRepos) -> None:
        JavaScriptApprovalTests.add_approvals_repos(builds)

    @staticmethod
    def add_approvals_repos(builds: AllRepos) -> None:
        language = 'JavaScript'

        repo = builds.add_source_repo('approvals', 'Approvals.NodeJS', ['master'],
                                      None,
                                      GitHubBuildConfig([]), language)
        repo = builds.add_source_repo('approvals', 'ApprovalTests.js.StarterProject', ['master'],
                                      None,
                                      GitHubBuildConfig([]), language)
