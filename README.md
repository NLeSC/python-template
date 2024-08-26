# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the [Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/) from the start.

Use this [Copier](https://copier.readthedocs.io) template to generate an empty Python package. Features include:

- Boilerplate unit tests and documentation,
- [Python static setup configuration](template/pyproject.toml.jinja),
- Open source software license,
- Continuous integration with [GitHub action workflows](template/.github/workflows) for building, testing, link checking and linting,
- Code style checking with [ruff](https://beta.ruff.rs/),
- [Editorconfig](template/.editorconfig),
- Usage and contribution documents:
  - [README.md](template/README.md.jinja) for package users,
  - [README.dev.md](template/README.dev.md.jinja) for package developer,
  - [project_setup.md](template/project_setup.md.jinja) with extensive documentation about project setup,
  - [Change log](template/%7B%25%20if%20AddChangeLog%20%25%7DCHANGELOG.md%7B%25%20endif%20%25%7D),
  - [Code of Conduct](template/CODE_OF_CONDUCT.md.jinja),
  - [Contributing guidelines](template/CONTRIBUTING.md.jinja),
- Continuous code quality and code coverage reporting using [Sonarcloud](https://sonarcloud.io/),
- Automatic creation of [issues](template/.github/next_steps) with instructions how to pass all GitHub action workflows and integrate with services like Zenodo and Read the Docs,
- Instructions how to make package [citable](.github/next_steps/%7B%25%20if%20AddCitation%20%25%7D02_citation.md%7B%25%20endif%20%25%7D.jinja)
- FAIR software recommendation badge,
- Optional [pre commit hook](template/README.dev.md.jinja#running-linters-locally) to catch lint errors early

## Badges

| fair-software.nl recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/nlesc/python-template) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/nlesc/python-template)](https://github.com/nlesc/python-template) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-python--template-00a3e3.svg)](https://research-software.nl/software/nlesc-python-template) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1310751.svg)](https://doi.org/10.5281/zenodo.1310751) |
| (5/5) checklist                    | &nbsp; |
| overall                            | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| &nbsp;                             | &nbsp; |
| **GitHub Actions**                 | &nbsp; |
| Citation metadata consistency      | [![cffconvert](https://github.com/nlesc/python-template/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/nlesc/python-template/actions/workflows/cffconvert.yml) |
| Link checker              | [![link-check](https://github.com/nlesc/python-template/actions/workflows/link-check.yml/badge.svg)](https://github.com/nlesc/python-template/actions/workflows/link-check.yml) |
| Tests                              | [![tests](https://github.com/nlesc/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/nlesc/python-template/actions/workflows/tests.yml) |

## How to use

There are multiple scenarios to use this template:

- [Scenario 1](#scenario-1-create-a-new-package): Generating a new package using template
- [Scenario 2](#scenario-2-apply-to-pre-existing-code): Applying the template to some pre-existing code
- [Scenario 3](#scenario-3-updating-a-template-made-package): Updating a package made with the template

In all three scenarios, you will need to install Copier first, which we
recommend doing with [`pipx`](https://github.com/pypa/pipx):
```shell
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install copier
```

> [!NOTE]
> Note that it is also possible to install Copier with regular `pip`, but that
> Copier will then be installed in your common environment and may cause
> conflicts with its dependencies, while `pipx` will install Copier in a
> separate and dedicated environment.

### Scenario 1: Create a new package


#### Step 1/2: Create the files and directory structure

Run `copier copy` with the template:

```shell
# Notes:
#   1. Make sure that `path/to/destination` is an empty directory
#   2. See table below for explanation of each question
#   3. The files will be generated in the specified destination directory
copier copy https://github.com/nlesc/python-template.git path/to/destination
```

Good job! Based on the profile and selected features, a package will be created in `path/to/destination`.

For an explanation of what's there, read on in the `project_setup.md` file.

### Scenario 2: Apply to pre-existing code

To apply the template to pre-existing code, you can use the same `copier copy`
command as when creating a new package, except that you point to the folder
containing your existing code rather than a new one:

```shell
copier copy https://github.com/nlesc/python-template.git path/to/existing/code
```

This works because if `path/to/destination` already exists, Copier will
update what is already there by either adding new files or updating
existing files. Copier will ask to overwrite any files that resulted in
conflicts. Especially if your files are already under version control, it is
recommended to answer 'yes' for all files, you will still be able to review
the changes suggested by the template.

### Scenario 3. Updating a template-made package

Copier provides the functionality for re-applying the template to a previously
created project using the `copier update` command. This has two effects:

1. Your project will be updated according to the latest version of the template
2. You can change any of your previous answers to apply these changes
   throughout your entire project.

> [!CAUTION]
> Do not manually update answers in `.copier-answers.yml`,
> as it will result in unexpected behavior.

```shell
cd path/to/project
copier update
```

If you don't want to change any of your answers, but only want to update your
project according to the latest template updates, you can provide the
`--skip-answered` option. This tells Copier to reuse all of your previous
answers, and simply bring in all updates from the template into
your current project, such as updating which Python versions are supported.
You will still be asked to answer any new questions that have been added to
the template since you last applied it.

```shell
copier update --skip-answered
```

## Examples

Many developers have gone before you in using this template to get started quickly. Check out their projects in the
list below:

1. Cerise: [https://github.com/MD-Studio/cerise](https://github.com/MD-Studio/cerise)
1. cerulean: [https://github.com/MD-Studio/cerulean](https://github.com/MD-Studio/cerulean)
1. cffconvert: [https://github.com/citation-file-format/cff-converter-python](https://github.com/citation-file-format/cff-converter-python)
1. fairtally: [https://github.com/fair-software/fairtally](https://github.com/fair-software/fairtally)
1. howfairis: [https://github.com/fair-software/howfairis](https://github.com/fair-software/howfairis)
1. matchms: [https://github.com/matchms/matchms](https://github.com/matchms/matchms)
1. MUSCLE 3: [https://github.com/multiscale/muscle3](https://github.com/multiscale/muscle3)
1. pycff: [https://github.com/citation-file-format/pycff](https://github.com/citation-file-format/pycff)
1. spec2vec: [https://github.com/iomega/spec2vec](https://github.com/iomega/spec2vec)
1. yatiml: [https://github.com/yatiml/yatiml](https://github.com/yatiml/yatiml)
1. _... And many more (see [this discussion](https://github.com/NLeSC/python-template/issues/48)). Make a PR to add your project here, or simply ping us in an issue!_


## How to contribute

Suggestions/improvements/edits are most welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request.
