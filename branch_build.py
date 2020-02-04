class RepoInfo:
    def __init__(self, user, project):
        self.user = user
        self.project = project

class BranchBuild:
    """
    Class that represents a row in the dashboard to represent the current status of builds
    for a particular branch in a particular repo
    """

    def __init__(self, user, project, branch, travis_com, appveyor_token, custom_appveyor_user):
        self.repo_info = RepoInfo(user, project)
        self.user = user
        self.project = project
        self.branch = branch

        # Travis info
        # see
        # https://devops.stackexchange.com/questions/1201/whats-the-difference-between-travis-ci-org-and-travis-ci-com
        if travis_com:
            self.travis_url_base_image = 'travis-ci.com'
            self.travis_url_base_target = self.travis_url_base_image
        else:
            self.travis_url_base_image = 'api.travis-ci.org'
            self.travis_url_base_target = 'travis-ci.org'

        # Appveyor info
        self.appveyor_token = appveyor_token
        self.appveyor_project = self.project.lower().replace('.', '-').replace('_', '-')
        if custom_appveyor_user:
            self.appveyor_user = custom_appveyor_user
        else:
            self.appveyor_user = self.user

    def user_link(self):
        text = self.user
        url = f"https://github.com/{self.user}?tab=repositories"
        return self.hyperlinked_text(text, url)

    def project_link(self):
        text = self.project
        url = f"https://github.com/{self.user}/{self.project}/"
        return self.hyperlinked_text(text, url)

    def network_link(self):
        text = 'network'
        url = f"https://github.com/{self.user}/{self.project}/network"
        return self.hyperlinked_text(text, url)

    def branch_link(self):
        text = self.branch
        url = f"https://github.com/{self.user}/{self.project}/commits/{self.branch}"
        return self.hyperlinked_text(text, url)

    @staticmethod
    def hyperlinked_image(link_label, image_url, target_url):
        return f'[![{link_label}]({image_url})]({target_url})'

    @staticmethod
    def hyperlinked_text(link_label, target_url):
        return f'[{link_label}]({target_url})'

    def travis_status(self):
        # There is currently no way that I can see for linking to the current build on the chosen branch.
        # See this, for requests from others for this: https://github.com/travis-ci/travis-ci/issues/5024
        # For the workaround I'm currently using, see https://stackoverflow.com/a/32946454/104370
        # We now link to to all branches for which there are Travis builds, allowing the user to
        # click on the branch of interest, and see its latest build.
        return self.hyperlinked_image(
            "Build Status",
            f"https://{self.travis_url_base_image}/{self.user}/{self.project}.svg?branch={self.branch}",
            f"https://{self.travis_url_base_target}/{self.user}/{self.project}/branches")

    def appveyor_status(self):
        if not self.appveyor_token:
            return '` `'

        return self.hyperlinked_image(
            "Build status",
            f"https://ci.appveyor.com/api/projects/status/{self.appveyor_token}/branch/{self.branch}?svg=true",
            f"https://ci.appveyor.com/project/{self.appveyor_user}/{self.appveyor_project}/branch/{self.branch}")

    def github_status(self):
        return self.hyperlinked_image(
            "Build Status",
            f'https://github.com/{self.user}/{self.project}/workflows/build/badge.svg?branch={self.branch}',
            f'https://github.com/{self.user}/{self.project}/actions?query=branch%3A{self.branch}')
