---
title: 'Next step: Linting'
---

Your repository has a [workflow]({{cookiecutter.repository}}/blob/main/.github/workflows/lint.yml) which [lints](https://en.wikipedia.org/wiki/Lint_(software)) your code in every push and when creating a pull request.

To make sure you have a proper linter configuration you need to follow the steps below.

1. Update `description` and `keywords` fields in <setup.cfg>.
1. Enable githook which will automatically lint your code in every commit. You can enable it by running the command below.

    ```shell
    git config --local core.hooksPath .githooks
    ```
