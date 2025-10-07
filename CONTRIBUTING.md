# Contributing guidelines

We welcome any kind of contribution to our software, from simple comment or question to a full fledged [pull request](https://help.github.com/articles/about-pull-requests/). Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

A contribution can be one of the following cases:

1. you have a question;
1. you think you may have found a bug (including unexpected behavior);
1. you want to make some kind of change to the code base (e.g. to fix a bug, to add a new feature, to update documentation).

The sections below outline the steps in each case.

## You have a question

1. use the search functionality [here](https://github.com/nlesc/python-template/issues) to see if someone already filed the same issue;
1. if your issue search did not yield any relevant results, make a new issue;
1. apply the "Question" label; apply other labels when relevant.

## You think you may have found a bug

1. use the search functionality [here](https://github.com/nlesc/python-template/issues) to see if someone already filed the same issue;
1. if your issue search did not yield any relevant results, make a new issue, making sure to provide enough information to the rest of the community to understand the cause and context of the problem. Depending on the issue, you may want to include:
    - the [SHA hashcode](https://help.github.com/articles/autolinked-references-and-urls/#commit-shas) of the commit that is causing your problem;
    - some identifying information (name and version number) for dependencies you're using;
    - information about the operating system;
1. apply relevant labels to the newly created issue.

## You want to make some kind of change to the code base

1. (**important**) this repository implements the best practices we recommend in the Python chapter of the [Guide](https://guide.esciencecenter.nl/#/language_guides/python). Check that your planned contribution is
in line with what is recommended there. If not, please [contribute to the guide](https://github.com/NLeSC/guide/blob/main/CONTRIBUTING.md) instead / as well, or at least create an issue there.
1. (**important**) announce your plan to the rest of the community _before you start working_. This announcement should be in the form of a (new) issue;
1. (**important**) wait until some kind of consensus is reached about your idea being a good idea;
1. if needed, fork the repository to your own Github profile and create your own feature branch off of the latest main commit. While working on your feature branch, make sure to stay up to date with the main branch by pulling in changes, possibly from the 'upstream' repository (follow the instructions [here](https://help.github.com/articles/configuring-a-remote-for-a-fork/) and [here](https://help.github.com/articles/syncing-a-fork/));
1. install dependencies (see the [development documentation](README.dev.md#create-a-virtual-environment));
1. make sure the existing tests still work by running ``pytest``. If project tests fail use ``pytest --keep-copied-projects`` to keep generated project files in `/tmp/pytest-*` and investigate;
1. add your own tests (if necessary);
1. update or expand the documentation;
1. update the `CHANGELOG.md` file with your change;
1. [push](http://rogerdudler.github.io/git-guide/) your feature branch to (your fork of) the Python Template repository on GitHub;
1. create the pull request, e.g. following the instructions [here](https://help.github.com/articles/creating-a-pull-request/).

In case you feel like you've made a valuable contribution, but you don't know how to write or run tests for it, or how to generate the documentation: don't let this discourage you from making the pull request; we can help you! Just go ahead and submit the pull request, but keep in mind that you might be asked to append additional commits to your pull request.

## You want to make a new release of the code base

To create a release you need write permission on the repository.

1. Check the author list in [`CITATION.cff`](CITATION.cff)
1. Update the version number in setup.cfg and CITATION.cff
1. Update the `CHANGELOG.md` to include changes made
1. Go to the [GitHub release page](https://github.com/nlesc/python-template/releases)
1. Press draft a new release button
1. Fill version, title and description field
1. Press the Publish Release button

Also a Zenodo entry will be made for the release with its own DOI.
