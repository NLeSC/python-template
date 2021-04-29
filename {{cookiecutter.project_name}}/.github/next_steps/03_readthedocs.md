---
title: 'Next step: Read the Docs'
---

Your Python package should have publicly available documentation, including API documentation for your users.
[Read the Docs](https://readthedocs.org) can host your user documentation for you.

To host the documentation of this repository please perform the following instructions:

1. go to [Read the Docs](https://readthedocs.org/dashboard/import/?)
1. log in with your GitHub account
1. find `{{ cookiecutter.github_organization }}/{{ cookiecutter.project_name }}` in list and press `+` button.
   * If repository is not listed,
      1. go to [Read the Docs GitHub app](https://github.com/settings/connections/applications/fae83c942bc1d89609e2)
      2. make sure {{ cookiecutter.github_organization }} has been granted access.
      3. reload repository list on Read the Docs import page
1. wait for the first build to be completed at <https://readthedocs.org/projects/{{ cookiecutter.project_name }}/builds>
1. check that the link of the documentation badge in the [README.md]({{ cookiecutter.repository }}) works

See [README.dev.md#]({{cookiecutter.repository}}/blob/main/README.dev.md#generating-the-api-docs) how to build documentation site locally.
