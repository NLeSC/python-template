---
title: 'Next step: Coverage'
---

Coverage reporting can be handled by [coverage.py](https://coverage.readthedocs.io) through a Github workflow. This repository is configured to produce a code coverage report on each push to main.

To configure the coverage reporting [GitHub Action workflow]({{cookiecutter.repository_url}}/blob/main/.github/workflows/build.yml) you must follow the steps below:

1. go to [Github Gist](https://gist.github.com/) to create a new gist
1. give it a useful description like '$projectname coverage badge'
1. copy the gist ID, this is the long alphanumeric string in the url that looks something like this: f635...06ae
1. paste the gist ID in the workflow yaml file: `.github/workflows/build.yml` after `gistID: `
1. to be able to run the analysis:
   1. a token with write rights to Gists must be created in your [Github settings](https://github.com/settings/tokens)
   1. the created token must be added as `GIST_TOKEN` to [secrets on GitHub](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.directory_name}}/settings/secrets/actions)
