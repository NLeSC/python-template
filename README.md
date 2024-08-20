# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the [Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/) from the start.

Use this [Copier](https://copier.readthedocs.io) template to generate an empty Python package. Features include:

- Boilerplate unit tests and documentation,
- [Python static setup configuration](template/pyproject.toml),
- Open source software license,
- Continuous integration with [GitHub action workflows](template/.github/workflows) for building, testing, link checking and linting,
- Code style checking with [ruff](https://beta.ruff.rs/),
- [Editorconfig](template/.editorconfig),
- Usage and contribution documents:
  - [README.md](template/README.md) for package users,
  - [README.dev.md](template/README.dev.md) for package developer,
  - [project_setup.md](template/project_setup.md) with extensive documentation about project setup,
  - [Change log](template/CHANGELOG.md),
  - [Code of Conduct](template/CODE_OF_CONDUCT.md),
  - [Contributing guidelines](template/CONTRIBUTING.md),
- Continuous code quality and code coverage reporting using [Sonarcloud](https://sonarcloud.io/),
- Automatic creation of [issues](template/.github/next_steps) with instructions how to pass all GitHub action workflows and integrate with services like Zenodo and Read the Docs,
- Instructions how to make package [citable](template/.github/next_steps/02_citation.md)
- FAIR software recommendation badge,
- Optional [pre commit hook](template/README.dev.md#running-linters-locally) to catch lint errors early

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
| MarkDown link checker              | [![markdown-link-check](https://github.com/nlesc/python-template/actions/workflows/markdown-link-check.yml/badge.svg)](https://github.com/nlesc/python-template/actions/workflows/markdown-link-check.yml) |
| Tests                              | [![tests](https://github.com/nlesc/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/nlesc/python-template/actions/workflows/tests.yml) |

## How to use

There are multiple scenarios to use this template:

1. Creating a new package based on the template
2. Applying the template to some pre-existing code
3. Updating a package made with the template

In all three cases, you will need to install copier first:
```shell
pipx install copier
```

### Option 1: Create a new package


#### Step 1/2: Generate the files and directory structure

Run `copier` with the template:

```shell
# Notes:
#   1. Make sure that `path/to/destination` is an empty directory
#   2. See table below for explanation of each question
#   3. The files will be generated in the specified destination directory
copier copy https://github.com/nlesc/python-template.git path/to/destination
```

| Name                      | Default value | Explanation |
| ------------------------- | ------------- | ----------- |
| package_name              | my_python_package | Name of the package. Avoid using spaces, dashes, or uppercase letters for the best experience across operating systems. This also will be used as the github repository name.|
| package_short_description | Short description of package | The information that you enter here will end up in the README, documentation, license, and pyproject.toml, so it may be a good idea to prepare something in advance. |
| keyword1                  | keyword1          | A term that describes your package. |
| keyword2                  | keyword2          | Another term that describes your package. |
| version                   | 0.1.0             | &nbsp; |
| github_organization       | &lt;my-github-organization&gt; | GitHub organization that will contain this project's repository. This can also be your GitHub user name. |
| license                   | Apache Software License 2.0 | The software license under which the code is made available.  |
| full_name                 | Jane Smith        | Your full name, e.g. _Jane Smith_. |
| email                     | yourname@esciencecenter.nl | Your (work) email address. |
| copyright_holder          | Netherlands eScience Center | Name(s) of the organization(s) or person(s) who hold the copyright of the software. |
| code_of_conduct_email     | yourname@esciencecenter.nl | Email address of the person who should be contacted in case of violations of the Code of Conduct. |

Once the project files have been generated, follow the steps outlined in
[template/next_steps.md](template/next_steps.md).

#### Step 2/2: Read about what was just generated

Good job! You have now generated the skeleton for your package:

```text
.
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── .copier-answers.yml
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   └── _templates
│       └── .gitignore
├── .editorconfig
├── .githooks
│   └── pre-commit
├── .github
│   ├── next_steps
│   │   ├── 01_sonarcloud_integration.md
│   │   ├── 02_citation.md
│   │   ├── 03_readthedocs.md
│   │   ├── 04_zenodo_integration.md
│   │   └── 05_linting.md
│   └── workflows
│       ├── build.yml
│       ├── cffconvert.yml
│       ├── documentation.yml
│       ├── markdown-link-check.yml
│       ├── next_steps.yml
│       └── sonarcloud.yml
├── .gitignore
├── MANIFEST.in
├── .mlc-config.json
├── next_steps.md
├── NOTICE
├── project_setup.md
├── pyproject.toml
├── README.dev.md
├── README.md
├── .readthedocs.yaml
├── sonar-project.properties
├── src
│   └── my_python_package
│       ├── __init__.py
│       └── my_module.py
├── tests
│   ├── __init__.py
│   ├── test_my_module.py
│   ├── test_project.py
│   └── test_values.py
└── .zenodo.json
```

For an explanation of what's there, read on in the [project_setup.md](template/project_setup.md) file.

### Option 2: Apply to pre-existing code

To apply the template to pre-existing code, you can use the same `copier copy`
command as when creating a new package, except that you point to the folder
containing your existing code rather than a new one:

```shell
copier copy https://github.com/nlesc/python-template.git path/to/existing/code
```

This works because if `path/to/destination` already exists, `copier` will
update what is already there by either adding new files or updating
existing files. Copier will ask to overwrite any files that resulted in
conflicts. Especially if your files are already under version control, it is
recommended to answer 'yes' for all files, you will still be able to review
the changes suggested by the template.

### Option 3. Updating a template-made package

Copier provides the functionality for re-applying the template to a previously
created project using the `copier update` command. This has two effects:

1. Your project will be updated according to the latest version of the template
2. You can change any of your previous answers to apply these changes
   throughout your entire project.

```shell
cd path/to/project
copier update
```

If you don't want to change any of your answers, but only want to update your
project according to the latest template updates, you can provide the
`--skip-answered` option. This tells copier to reuse all of your previous
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
