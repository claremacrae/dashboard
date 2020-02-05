from build_table import BuildTable
from build_badges import BuildBadges
from builds import AllRepos
from my_builds import add_all_builds


def create_readme(builds):
    table = BuildTable()
    table.write_readme(builds)


def create_badges(builds):
    table = BuildBadges()
    table.write_badges(builds)


def update_output_files():
    # See also https://travis-ci.com/dashboard

    builds = AllRepos()
    add_all_builds(builds)

    create_readme(builds)
    create_badges(builds)


if __name__ == '__main__':
    update_output_files()
