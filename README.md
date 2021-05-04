# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the
[Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/)
from the start.

Use this [Cookiecutter](https://cookiecutter.readthedocs.io) template to generate
an empty Python package. Features include:

- Boilerplate unit tests and documentation,
- [Python static setup configuration]({{cookiecutter.directory_name}}/setup.cfg),
- Open source software license,
- Continuous integration with [GitHub action workflows]({{cookiecutter.directory_name}}/.github/workflows) for building, testing, link checking and linting,
- Code style checking with [prospector](https://pypi.org/project/prospector/),
- [Editorconfig]({{cookiecutter.directory_name}}/.editorconfig),
- Usage and contribution documents:
  - [README.md]({{cookiecutter.directory_name}}/README.md) for package users,
  - [README.dev.md]({{cookiecutter.directory_name}}/README.dev.md) for package developer,
  - [README.project_layout_explained.md]({{cookiecutter.directory_name}}/README.project_layout_explained.md) with extensive documentation about project setup,
  - [CHANGELOG.md]({{cookiecutter.directory_name}}/CHANGELOG.md),
  - [Code of Conduct]({{cookiecutter.directory_name}}/CODE_OF_CONDUCT.md),
  - [Contributing guidelines]({{cookiecutter.directory_name}}/CONTRIBUTING.md),
- Continuous code quality and code coverage reporting using [Sonarcloud](https://sonarcloud.io/),
- Automatic creation of [issues]({{cookiecutter.directory_name}}/.github/next_steps) with instructions how to pass all GitHub action workflows and integrate with services like Zenodo and Read the Docs,
- Instructions how to make package [citable]({{cookiecutter.directory_name}}/.github/next_steps/04_citation.md)
- FAIR software recommendation badge,
- Optional [pre commit hook]({{cookiecutter.directory_name}}/README.dev.md#running-linters-locally) to catch lint errors early

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

### Step 1/3: Install `cookiecutter`

We recommend installing `cookiecutter` in user space as per `cookiecutter`'s instructions. This way, you don't have to
install `cookiecutter` for every new project.

```shell
python3 -m pip install --user --upgrade cookiecutter
```

### Step 2/3: Generate the files and directory structure

Run `cookiecutter` with the template:

```shell
# Notes:
#   1. See table below for explanation of each question
#   2. The files will be generated in a new directory
cookiecutter https://github.com/nlesc/python-template.git
```

| Name                      | Default value | Explanation |
| ------------------------- | ------------- | ----------- |
| directory_name              | my-python-project | Name of the directory that contains the package. Avoid using spaces or uppercase letters for the best experience across operating systems. To get an impression of what will be generated, see the directory tree [below](https://github.com/NLeSC/python-template#step-33-read-about-what-was-just-generated) |
| package_name              | my_python_package | Name of the package. Avoid using spaces, dashes, or uppercase letters for the best experience across operating systems. |
| package_short_description | &nbsp;            | The information that you enter here will end up in the README, documentation, license, and setup.cfg, so it may be a good idea to prepare something in advance. |
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
[{{cookiecutter.directory_name}}/README.next_steps.md]({{cookiecutter.directory_name}}/README.next_steps.md).

### Step 3/3: Read about what was just generated

Good job! You have now generated the skeleton for your package:

```text
my-python-project/
├── .bumpversion.cfg
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── _static
│   │   └── theme_overrides.css
│   └── _templates
│       └── .gitignore
├── .editorconfig
├── .githooks
│   └── pre-commit
├── .github
│   ├── next_steps
│   │   ├── 01_sonarcloud_integration.md
│   │   ├── 02_citation.md
│   │   ├── 03_readthedocs.md
│   │   ├── 04_zenodo_integration.md
│   │   └── 05_linting.md
│   └── workflows
│       ├── build.yml
│       ├── cffconvert.yml
│       ├── lint.yml
│       ├── markdown-link-check.yml
│       ├── next_steps.yml
│       └── sonarcloud.yml
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── .mlc-config.json
├── my_python_package
│   ├── __init__.py
│   ├── my_module.py
│   └── __version__.py
├── NOTICE
├── .prospector.yml
├── .pylintrc
├── pyproject.toml
├── README.dev.md
├── README.md
├── README.next_steps.md
├── README.project_layout_explained.md
├── setup.cfg
├── setup.py
├── sonar-project.properties
└── tests
    ├── __init__.py
    └── test_my_module.py
```

For an explanation of what's there, read on in the [README.project_layout_explained.md]({{cookiecutter.directory_name}}/README.project_layout_explained.md) file.
There are also instructions on how to [apply the template to an existing Python package](README.add_to_existing_package.md).

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
1. _... And many more. Make a PR to add your project here!_


## How to contribute

Suggestions/improvements/edits are most welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request.
