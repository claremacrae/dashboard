# GitHub Actions

<!-- toc -->
## Contents

  * [Reference](#reference)
    * [General](#general)
    * [GitHub Actions  Reference](#github-actions--reference)
    * [Schema](#schema)
    * [Specific Actions](#specific-actions)
  * [Finding Info](#finding-info)
    * [Searches](#searches)
    * [Examples](#examples)
  * [Specific Topics](#specific-topics)
    * [Composite run steps](#composite-run-steps)
    * [Cron Jobs](#cron-jobs)<!-- endToc -->

## Reference

### General

- [GitHub Actions, the missing notes](https://skypjack.github.io/2019-10-23-gh-greets-qt/)
- [Usage on GitHub Actions with xvfb · Issue #147 · juliangruber/browser-run](https://github.com/juliangruber/browser-run/issues/147)
- [GitHub Marketplace · Actions to improve your workflow](https://github.com/marketplace?type=actions)

### GitHub Actions  [Reference](https://docs.github.com/en/free-pro-team@latest/actions/reference)

- [Workflow syntax for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
- [Specifications for GitHub-hosted runners](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners)
  - [Supported software](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners#supported-software)
- [Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)
- [Environment variables](https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions)
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#example-using-multiple-events-with-activity-types-or-configuration)

### Schema

- [Workflow Schema](https://json.schemastore.org/github-workflow)
- [Action Schema](https://json.schemastore.org/github-action)

### Specific Actions

- [actions/checkout](https://github.com/actions/checkout): Action for checking out a repo
- [actions/runner](https://github.com/actions/runner): The runner is the application that runs a job from a GitHub
  Actions workflow
- [actions/starter-workflows](https://github.com/actions/starter-workflows): Accelerating new GitHub Actions workflows

## Finding Info

### Searches

- [Search · search_term path:/.github/workflows/](https://github.com/search?q=search_term+path%3A%2F.github%2Fworkflows%2F+extension%3Ayml&type=Code)
- [New Search · search_term path:/.github/workflows/](https://cs.github.com/?scopeName=All+repos&scope=&q=search_term+path%3A%2F.github%2Fworkflows%2F+path%3A*.yml)
- [github actions qt5 - Google Search](https://www.google.com/search?client=safari&rls=en&q=github+actions+qt5&ie=UTF-8&oe=UTF-8)

### Examples

- [doctest/main.yml at master · onqtam/doctest](https://github.com/onqtam/doctest/blob/master/.github/workflows/main.yml)
- [reproc/main.yml at master · DaanDeMeyer/reproc](https://github.com/DaanDeMeyer/reproc/blob/master/.github/workflows/main.yml)
- [libgit2/main.yml at main · libgit2/libgit2](https://github.com/libgit2/libgit2/blob/main/.github/workflows/main.yml)
  - shows that matrices can be objects, and not just strings
- [How to share matrix between jobs](https://github.community/t/how-to-share-matrix-between-jobs/128595)

## Specific Topics

### Composite run steps

- Docs: [Creating a composite run steps action](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/creating-a-composite-run-steps-action)
- Stack Overflow
  - [Reuse composite run steps action in same repo](https://stackoverflow.com/a/64079155/104370)
  - [How to us snippets in github action workflow file to avoid duplicates?
    ](https://stackoverflow.com/questions/60544181/how-to-us-snippets-in-github-action-workflow-file-to-avoid-duplicates)
- Video: [GitHub Actions - Composite Run Steps FIRST LOOK](https://www.youtube.com/watch?v=OqJyrZUUGTw)
- Issue: [Next Steps for Fully Functioning Composite Actions](https://github.com/actions/runner/issues/646) - include
  examples of what you **can** do
- [GitHub Actions: reusable workflows is generally available](https://github.blog/2021-11-29-github-actions-reusable-workflows-is-generally-available/)

### Cron Jobs

- How to not run cron jobs in forks
  - Searsch: [GitHub Actions don't run cron on forks](https://www.google.com/search?client=safari&rls=en&q=GitHub+Actions+don%27t+run+cron+on+forks)
  - [Do not run cron workflows in forks](https://github.community/t/do-not-run-cron-workflows-in-forks/17636)
