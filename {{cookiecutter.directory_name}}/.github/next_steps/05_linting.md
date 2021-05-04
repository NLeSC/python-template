---
title: 'Next step: Linting'
---

Your repository has a [workflow]({{ cookiecutter.repository }}/blob/main/.github/workflows/build.yml) which [lints](https://en.wikipedia.org/wiki/Lint_(software)) your code after every push and when creating a pull request.

Linter workflow may fail if `description` or `keywords` field in [setup.cfg]({{ cookiecutter.repository }}/blob/main/setup.cfg) is empty. Please update these fields. To validate your changes run:

```shell
prospector
```

Enabling [githook](https://git-scm.com/docs/githooks) will automatically lint your code in every commit. You can enable it by running the command below.

```shell
git config --local core.hooksPath .githooks
```
