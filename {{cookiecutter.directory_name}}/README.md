## Badges

(Customize these badges with your own links, and check https://shields.io/ or https://badgen.net/ to see which other badges are available.)

| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)]({{cookiecutter.repository}}) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/{{cookiecutter.github_organization}}/{{cookiecutter.directory_name}})]({{cookiecutter.repository}}) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-{{cookiecutter.package_name}}-00a3e3.svg)](https://www.research-software.nl/software/{{cookiecutter.package_name}}) [![workflow pypi badge](https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg?colorB=blue)](https://pypi.python.org/project/{{cookiecutter.package_name}}/) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>) |
| (5/5) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization}}_{{cookiecutter.directory_name}}&metric=alert_status)](https://sonarcloud.io/dashboard?id={{cookiecutter.github_organization}}_{{cookiecutter.directory_name}}) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization}}_{{cookiecutter.directory_name}}&metric=coverage)](https://sonarcloud.io/dashboard?id={{cookiecutter.github_organization}}_{{cookiecutter.directory_name}}) |
| Documentation                      | [![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.directory_name}}/badge/?version=latest)](https://{{cookiecutter.directory_name}}.readthedocs.io/en/latest/?badge=latest) |
| **GitHub Actions**                 | &nbsp; |
| Build                              | [![build]({{cookiecutter.repository}}/actions/workflows/build.yml/badge.svg)]({{cookiecutter.repository}}/actions/workflows/build.yml) |
|  Metadata consistency              | [![cffconvert]({{cookiecutter.repository}}/actions/workflows/cffconvert.yml/badge.svg)]({{cookiecutter.repository}}/actions/workflows/cffconvert.yml) |
| Lint                               | [![lint]({{cookiecutter.repository}}/actions/workflows/lint.yml/badge.svg)]({{cookiecutter.repository}}/actions/workflows/lint.yml) |
| SonarCloud                         | [![sonarcloud]({{cookiecutter.repository}}/actions/workflows/sonarcloud.yml/badge.svg)]({{cookiecutter.repository}}/actions/workflows/sonarcloud.yml) |
| MarkDown link checker              | [![markdown-link-check]({{cookiecutter.repository}}/actions/workflows/markdown-link-check.yml/badge.svg)]({{cookiecutter.repository}}/actions/workflows/markdown-link-check.yml) |

## How to use {{ cookiecutter.package_name }}

{{ cookiecutter.package_short_description }}

The project setup is documented in [README.project_layout_explained.md](README.project_layout_explained.md). Feel free to remove this document (and/or the link to this document) if you don't need it.

## Installation

To install {{ cookiecutter.package_name }} from GitHub repository, do:

```console
git clone {{ cookiecutter.repository }}.git
cd {{ cookiecutter.directory_name }}
python3 -m pip install .
```

## Documentation

Include a link to your project's full documentation here.

## Contributing

If you want to contribute to the development of {{ cookiecutter.package_name }},
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
