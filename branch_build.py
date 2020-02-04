import dashboard_utilities

class RepoInfo:
    def __init__(self, user, project, branch):
        self.user = user
        self.project = project
        self.branch = branch

    def user_link(self):
        text = self.user
        url = f"https://github.com/{self.user}?tab=repositories"
        return dashboard_utilities.hyperlinked_text(text, url)

    def project_link(self):
        text = self.project
        url = f"https://github.com/{self.user}/{self.project}/"
        return dashboard_utilities.hyperlinked_text(text, url)

    def network_link(self):
        text = 'network'
        url = f"https://github.com/{self.user}/{self.project}/network"
        return dashboard_utilities.hyperlinked_text(text, url)

    def branch_link(self):
        text = self.branch
        url = f"https://github.com/{self.user}/{self.project}/commits/{self.branch}"
        return dashboard_utilities.hyperlinked_text(text, url)


class TravisBuildInfo:
    def __init__(self, repo_info, travis_com):
        self.repo_info = repo_info
        # Travis info
        # see
        # https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if travis_com:
            self.travis_url_base_image = 'travis-ci.com'
            self.travis_url_base_target = self.travis_url_base_image
        else:
            self.travis_url_base_image = 'api.travis-ci.org'
            self.travis_url_base_target = 'travis-ci.org'

    def travis_status(self):
        # There is currently no way that I can see for linking to the current build on the chosen branch.
        # See this, for requests from others for this: https://github.com/travis-ci/travis-ci/issues/5024
        # For the workaround I'm currently using, see https://stackoverflow.com/a/32946454/104370
        # We now link to to all branches for which there are Travis builds, allowing the user to
        # click on the branch of interest, and see its latest build.
        return dashboard_utilities.hyperlinked_image(
            "Build Status",
            f"https://{self.travis_url_base_image}/{self.repo_info.user}/{self.repo_info.project}.svg?branch={self.repo_info.branch}",
            f"https://{self.travis_url_base_target}/{self.repo_info.user}/{self.repo_info.project}/branches")


class AppveyorBuildInfo:
    def __init__(self, repo_info, appveyor_token, custom_appveyor_user):
        self.repo_info = repo_info
        self.appveyor_token = appveyor_token
        self.appveyor_project = repo_info.project.lower().replace('.', '-').replace('_', '-')
        if custom_appveyor_user:
            self.appveyor_user = custom_appveyor_user
        else:
            self.appveyor_user = repo_info.user

    def appveyor_status(self):
        if not self.appveyor_token:
            return '` `'

        return dashboard_utilities.hyperlinked_image(
            "Build status",
            f"https://ci.appveyor.com/api/projects/status/{self.appveyor_token}/branch/{self.repo_info.branch}?svg=true",
            f"https://ci.appveyor.com/project/{self.appveyor_user}/{self.appveyor_project}/branch/{self.repo_info.branch}")


class GitHubBuildInfo:
    def __init__(self, repo_info):
        self.repo_info = repo_info

    def github_status(self):
        return dashboard_utilities.hyperlinked_image(
            "Build Status",
            f'https://github.com/{self.repo_info.user}/{self.repo_info.project}/workflows/build/badge.svg?branch={self.repo_info.branch}',
            f'https://github.com/{self.repo_info.user}/{self.repo_info.project}/actions?query=branch%3A{self.repo_info.branch}')


class BranchBuild:
    """
    Class that represents a row in the dashboard to represent the current status of builds
    for a particular branch in a particular repo
    """

    def __init__(self, user, project, branch, travis_com, appveyor_token, custom_appveyor_user):
        self.repo_info = RepoInfo(user, project, branch)

        self.travis_build_info = TravisBuildInfo(self.repo_info, travis_com)

        # Appveyor info
        self.appveyor_build_info = AppveyorBuildInfo(self.repo_info, appveyor_token, custom_appveyor_user)

        self.github_build_info = GitHubBuildInfo(self.repo_info)
