#! /usr/bin/env python3

from scripts.build_table import BuildTable
from scripts.create_build_badges import BuildBadges
from scripts.all_repos import AllRepos
from scripts.my_builds import add_all_repos


def create_readme(builds):
    table = BuildTable()
    table.write_readme(builds)


def create_badges(builds):
    table = BuildBadges()
    table.write_badges(builds)


def update_output_files():
    builds = AllRepos()
    add_all_repos(builds)

    create_readme(builds)
    create_badges(builds)


if __name__ == '__main__':
    update_output_files()
