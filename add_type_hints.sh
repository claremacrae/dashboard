#!/bin/sh

# https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881
#monkeytype run update_markdown_files.py
#monkeytype list-modules

monkeytype apply scripts.all_repos
monkeytype apply scripts.ci_configs
monkeytype apply scripts.create_build_badges
monkeytype apply scripts.create_build_table
monkeytype apply scripts.dashboard_utilities
monkeytype apply scripts.my_builds
monkeytype apply scripts.repo_and_builds
