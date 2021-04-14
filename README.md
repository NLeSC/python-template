# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the
[Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/)
from the start.

Use this [Cookiecutter](https://cookiecutter.readthedocs.io) template to generate
an empty Python package. Features include:

- Boilerplate tests and documentation,
- [Python setup configuration]({{ cookiecutter.derived.project_name }}/setup.py),
- Open source software license,
- [Default Github actions]({{ cookiecutter.derived.project_name }}/.github/workflows) for building, testing and deployment
- Code style checking,
- [Editorconfig]({{ cookiecutter.derived.project_name }}/.editorconfig),
- Miscellaneous files, such as [Change log]({{ cookiecutter.derived.project_name }}/CHANGELOG.rst), [Code of Conduct]({{ cookiecutter.derived.project_name }}/CODE_OF_CONDUCT.rst), and [Contributing guidelines]({{ cookiecutter.derived.project_name }}/CONTRIBUTING.rst),
- A [README]({{ cookiecutter.derived.project_name }}/README.rst) and [a separate document]({{ cookiecutter.derived.project_name }}/project_setup.rst) with extensive documentation about project setup.

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
| MarkDown link checker              | [![workflow mlc badge](https://github.com/nlesc/python-template/workflows/markdown-link-checker/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3A%22markdown-link-checker%22) |
| Citation metadata consistency      | [![workflow cffconvert badge](https://github.com/nlesc/python-template/workflows/cffconvert/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3A%22cffconvert%22) |
| Unit tests                         | [![workflow tests badge](https://github.com/nlesc/python-template/workflows/tests/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3Atests) |

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
| project_name              | My Python Project  | Full project/package name.  |
| project_slug              | my_python_project  | This will be the name of the directory to be created and the git repository. It is safest not to use dashes (-) or spaces in this name. |
| project_short_description |   | The information that you enter here will end up in the README, documentation, license, and setup.py, so it may be a good idea to prepare something in advance. |
| version                   | 0.1.0  |   |
| github_organization       |   | GitHub organization that will contain this project's repository. This can also be your github user name. |
| open_source_license       | Apache 2.0 (1)  | The software license under which the code is made available.  |
| apidoc                    | no (1)  | Add support for automatically generating a module index from the `docstrings` in your Python package (look at the [scriptcwl package](http://scriptcwl.readthedocs.io/en/latest/apidocs/scriptcwl.html) for an example).
| full_name                 | John Smith  | Your full name, e.g. _John Smith_.   |
| email                     | yourname@esciencecenter.nl | Your (work) email address  |
| copyright_holder          |   | Name(s) of the organization(s) or person(s) who hold the copyright of the software (e.g., Netherlands eScience Center).  |
| code_of_conduct_email     | yourname@esciencecenter.nl | Email address of the person who should be contacted in case of violations of the Code of Conduct.  |

### Step 3/3: Read about what was just generated

Good job! You have now generated the skeleton for your package. For an explanation of what's there, read on in the [project_setup.rst]({{ cookiecutter.derived.project_name }}/project_setup.rst) file.

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
