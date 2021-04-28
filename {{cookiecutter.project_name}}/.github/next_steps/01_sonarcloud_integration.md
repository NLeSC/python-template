---
title: 'Next step: Sonarcloud integration'
labels: enhancement
---

Continuous code quality can be handled by many services for `NLeSC/python-template` we chose [Sonarcloud](https://sonarcloud.io/).
[Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report on each push.

Sonarcloud must be configured for the analysis to work

1. go to [Sonarcloud](https://sonarcloud.io/projects/create)
2. login with your GitHub account
3. add organization or reuse existing one
4. set up repository
5. go to [new code definition administration page](https://sonarcloud.io/project/new_code?id={{ cookiecutter.github_organization }}_{{ cookiecutter.project_name }}) and select `Number of days` option

The analysis will be run by [GitHub Action workflow](.github/workflows/sonarcloud.yml)
To be able to run the analysis, a token must be created at [Sonarcloud account](https://sonarcloud.io/account/security/) and this token must be added as `SONAR_TOKEN` to [secrets on GitHub](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_name }}/settings/secrets/actions)
