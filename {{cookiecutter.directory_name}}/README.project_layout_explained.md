# Project layout explained

Here we provide some details about the project setup. Most of the choices are explained in the
[guide](https://guide.esciencecenter.nl). Links to the relevant sections are included below. Feel free to remove this
text when the development of the software package takes off.

For a quick reference on software development, we refer to [the software guide
checklist](https://guide.esciencecenter.nl/#/best_practices/checklist).

## Python versions

This repository is set up with Python versions:

- 3.6
- 3.7
- 3.8
- 3.9

Add or remove Python versions based on project requirements. See [the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python) for more information about Python
versions.

## Package management and dependencies

You can use either pip or conda for installing dependencies and package management. This repository does not force you
to use one or the other, as project requirements differ. For advice on what to use, please check [the relevant section
of the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=dependencies-and-package-management).

- Runtime dependencies should be added to `setup.cfg` in the `install_requires` list under `[options]`.
- Development dependencies should be added to `setup.cfg` in one of the lists under `[options.extras_require]`.

## Packaging/One command install

You can distribute your code using PyPI.
[The guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code) can
help you decide which tool to use for packaging.

## Testing and code coverage

- Tests should be put in the `tests` folder.
- The `tests` folder contains:
  - Example tests that you should replace with your own meaningful tests (file: `test_my_module.py`)
- The testing framework used is [PyTest](https://pytest.org)
  - [PyTest introduction](http://pythontesting.net/framework/pytest/pytest-introduction/)
  - PyTest is listed as a development dependency, and can thus be installed with `pip3 install --editable .[dev]`
- Tests can be run with `pytest`
  - This is configured in `setup.cfg`
- The project uses [GitHub action workflows](https://docs.github.com/en/actions) to automatically run tests on GitHub infrastructure against multiple Python versions
  - Workflows can be found in [`.github/workflows`](.github/workflows/)
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=testing)

## Documentation

- Documentation should be put in the [`docs/`](docs/) directory. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
- We recommend writing the documentation using Restructured Text (reST) and Google style docstrings.
  - [Restructured Text (reST) and Sphinx CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
  - [Google style docstring examples](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- The documentation is set up with the ReadTheDocs Sphinx theme.
  - Check out its [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/).
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=writingdocumentation)

## Coding style conventions and code quality

- Check your code style with `prospector`
- You may need run `pip install --editable .[dev]` first, to install the required dependencies
- You can use `yapf` to fix the readability of your code style and `isort` to format and group your imports
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=coding-style-conventions)

## Continuous code quality

[Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report

- `sonar-project.properties` is the SonarCloud [configuration](https://docs.sonarqube.org/latest/analysis/analysis-parameters/) file
- `.github/workflows/sonarcloud.yml` is the GitHub action workflow which performs the SonarCloud analysis

## Package version number

- We recommend using [semantic versioning](https://guide.esciencecenter.nl/#/best_practices/releases?id=semantic-versioning).
- For convenience, the package version is stored in a single place: `{{ cookiecutter.directory_name }}/.bumpversion.cfg`.
  For updating the version number, make sure the dev dependencies are installed and run `bumpversion patch`,
  `bumpversion minor`, or `bumpversion major` as appropriate.
- Don't forget to update the version number before [making a release](https://guide.esciencecenter.nl/#/best_practices/releases)!

## Logging

- We recommend using the logging module for getting useful information from your module (instead of using print).
- The project is set up with a logging example.
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=logging)

## CHANGELOG.md

- Document changes to your software package
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/releases?id=changelogmd)

## CITATION.cff

- To allow others to cite your software, add a `CITATION.cff` file
- It only makes sense to do this once there is something to cite (e.g., a software release with a DOI).
- Follow the [making software citable](https://guide.esciencecenter.nl/#/citable_software/making_software_citable) section in the guide.

## CODE_OF_CONDUCT.md

- Information about how to behave professionally
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=code-of-conduct)

## CONTRIBUTING.md

- Information about how to contribute to this software package
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=contribution-guidelines)

## MANIFEST.in

- List non-Python files that should be included in a source distribution
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code)

## NOTICE

- List of attributions of this project and Apache-license dependencies
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/licensing?id=notice)
