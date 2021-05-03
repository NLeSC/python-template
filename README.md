# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the
[Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/)
from the start.

Use this [Cookiecutter](https://cookiecutter.readthedocs.io) template to generate
an empty Python package. Features include:

- Boilerplate tests and documentation,
- [Python setup configuration]({{cookiecutter.directory_name}}/setup.py),
- Open source software license,
- [Default Github actions]({{cookiecutter.directory_name}}/.github/workflows) for building, testing and deployment
- Code style checking,
- [Editorconfig]({{cookiecutter.directory_name}}/.editorconfig),
- Miscellaneous files, such as [Change log]({{cookiecutter.directory_name}}/CHANGELOG.md), [Code of Conduct]({{cookiecutter.directory_name}}/CODE_OF_CONDUCT.md), and [Contributing guidelines]({{cookiecutter.directory_name}}/CONTRIBUTING.md),
- A [README]({{cookiecutter.directory_name}}/README.md) and [a separate document]({{cookiecutter.directory_name}}/project_setup.md) with extensive documentation about project setup.
- Continuous code quality and code coverage reporting using [Sonarcloud](https://sonarcloud.io/)

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
| package_name              | my_python_package | Name of the package. Avoid using spaces, dashes, or uppercase letters for the best experience across operating systems. |
| directory_name              | my-python-project | Name of the project that contains the package. Avoid using spaces or uppercase letters for the best experience across operating systems. |
| package_short_description | &nbsp;            | The information that you enter here will end up in the README, documentation, license, and setup.cfg, so it may be a good idea to prepare something in advance. |
| version                   | 0.1.0             | &nbsp; |
| github_organization       | &lt;my-github-organization&gt; | GitHub organization that will contain this project's repository. This can also be your GitHub user name. |
| license                   | Apache Software License 2.0 | The software license under which the code is made available.  |
| full_name                 | John Smith        | Your full name, e.g. _John Smith_. |
| email                     | yourname@esciencecenter.nl | Your (work) email address. |
| copyright_holder          | Netherlands eScience Center | Name(s) of the organization(s) or person(s) who hold the copyright of the software. |
| code_of_conduct_email     | yourname@esciencecenter.nl | Email address of the person who should be contacted in case of violations of the Code of Conduct. |

Once the project files have been generated, follow the steps outlined in
[{{cookiecutter.directory_name}}/next_steps.md]({{cookiecutter.directory_name}}/next_steps.md).

### Step 3/3: Read about what was just generated

Good job! You have now generated the skeleton for your package:

```text
my-python-project/
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
├── LICENSE
├── MANIFEST.in
├── my_python_package
│   ├── __init__.py
│   ├── my_module.py
│   └── __version__.py
├── NOTICE
├── project_setup.md
├── README.md
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    └── test_my_module.py
```

For an explanation of what's there, read on in the [project_setup.md]({{cookiecutter.directory_name}}/project_setup.md) file.

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
