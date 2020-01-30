from build_table import BuildTable
from build_badges import BuildBadges
from builds import Builds
from my_builds import add_all_builds


def create_readme():
    builds = Builds()

    add_all_builds(builds)

    table = BuildTable()
    table.write_readme(builds)


def create_badges():
    builds = Builds()

    add_all_builds(builds)

    table = BuildBadges()
    table.write_badges(builds)


def update_output_files():
    # See also https://travis-ci.com/dashboard
    create_readme()
    create_badges()


if __name__ == '__main__':
    update_output_files()
