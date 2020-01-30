from build_table import BuildTable
from builds import Builds
from my_builds import add_all_builds


def create_readme():
    builds = Builds()

    add_all_builds(builds)

    table = BuildTable()
    table.write_readme(builds)


if __name__ == '__main__':
    # See also https://travis-ci.com/dashboard
    create_readme()
