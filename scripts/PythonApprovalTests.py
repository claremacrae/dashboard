from scripts.implementation.all_repos import AllRepos
from scripts.implementation.github_configs import GitHubBuildConfig


class PythonApprovalTests:
    @staticmethod
    def add_all_repos(builds: AllRepos) -> None:
        # PythonApprovalTests.add_approvals_repos(builds)
        pass

    @staticmethod
    def add_approvals_repos(builds: AllRepos) -> None:
        python = 'Python'
        default_workflows = ['Test', 'on-push-do-doco']  # We only show the publishing workflow in source repo
        parent_git_hub_build_config = GitHubBuildConfig(default_workflows + ['Upload Python Package'], False)
        repo = builds.add_source_repo('approvals', 'ApprovalTests.Python', ['master'], None,
                                      parent_git_hub_build_config,
                                      language=python)
        fork_git_hub_build_config = GitHubBuildConfig(default_workflows, False)
        builds.add_forked_repo(repo, github_build_info=fork_git_hub_build_config)

        repo = builds.add_source_repo('approvals', 'ApprovalTests.Python.PytestPlugin', ['master'], None,
                                      GitHubBuildConfig(['Test'], False), language=python)
        builds.add_forked_repo(repo)
