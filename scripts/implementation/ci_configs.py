from typing import List, Union

from scripts.implementation import dashboard_utilities
from scripts.implementation.appveyor_configs import AppveyorBuildConfig
from scripts.implementation.dashboard_utilities import hyperlinked_text, encode_string
from scripts.implementation.github_repo_info import GitHubRepoInfo


class GitHubWorkflow:
    def __init__(self, name: str, tied_to_branch: bool):
        self.name = name
        self.tied_to_branch = tied_to_branch

    def badge_image_url(self, user: str, project: str, branch: str):
        encoded_workflow_name = encode_string(self.name)
        result = f'https://github.com/{user}/{project}/workflows/{encoded_workflow_name}/badge.svg'
        if self.tied_to_branch > 0:
            result += f'?branch={branch}'
        return result

    def badge_target_url(self, user: str, project: str, branch: str):
        result = f'https://github.com/{user}/{project}/actions?query='
        if self.tied_to_branch > 0:
            result += f'branch%3A{branch}+'

        encoded_workflow_name = self.name
        if ' ' in self.name:
            encoded_workflow_name = '%22' + self.name.replace(' ', '+') + '%22'
        result += f'workflow%3A{encoded_workflow_name}'

        return result

    def badge(self, user: str, project: str, branch: str):
        return dashboard_utilities.hyperlinked_image(
            "Build Status",
            self.badge_image_url(user, project, branch),
            self.badge_target_url(user, project, branch))


class GitHubBuildConfig:
    def __init__(self, workflow_names=None, tied_to_branch: bool = True) -> None:
        if workflow_names is None:
            workflow_names = ['build']
        self.workflows = []
        for workflow in workflow_names:
            self.add_workflow(workflow, tied_to_branch)

    def add_workflow(self, workflow_name: str, tied_to_branch: bool):
        self.workflows.append(GitHubWorkflow(workflow_name, tied_to_branch))

    @staticmethod
    def column_title() -> str:
        return F'GitHub / {hyperlinked_text("Links", "/links/github_actions.md")}'

    def status(self, repo_info: GitHubRepoInfo, branch: str) -> str:
        user = repo_info.user
        project = repo_info.project
        result = ''
        for workflow in self.workflows:
            if len(result) > 0:
                result += "  "
            result += workflow.badge(user, project, branch)
        return result


class RepoAndBuilds:
    """
    Class that represents a particular repository and all its active branches and its CI builds
    """

    def __init__(self, repo_info: GitHubRepoInfo, appveyor_build_info: AppveyorBuildConfig,
                 github_build_info: GitHubBuildConfig) -> None:
        self.repo_info = repo_info
        self.appveyor_build_info = appveyor_build_info
        self.github_build_info = github_build_info

    def all_builds(self) -> List[Union[AppveyorBuildConfig, GitHubBuildConfig]]:
        return [
            self.appveyor_build_info,
            self.github_build_info,
        ]
