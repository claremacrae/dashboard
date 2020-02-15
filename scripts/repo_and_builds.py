from scripts import dashboard_utilities


class RepoInfo:
    def __init__(self, user, project, branches, type):
        self.user = user
        self.project = project
        self.branches = branches
        self.type = type

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

    def branch_link(self, branch):
        text = branch
        url = f"https://github.com/{self.user}/{self.project}/commits/{branch}"
        return dashboard_utilities.hyperlinked_text(text, url)


class RepoAndBuilds:
    """
    Class that represents a particular repository and all its active branches and its CI builds
    """

    def __init__(self, repo_info, travis_build_info, appveyor_build_info, github_build_info):
        self.repo_info = repo_info
        self.travis_build_info = travis_build_info
        self.appveyor_build_info = appveyor_build_info
        self.github_build_info = github_build_info
