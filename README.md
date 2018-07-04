Netherlands eScience Center Python Template
===========================================

Spend less time setting up and configuring your new Python packages and comply with the
[Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/)
from the start.

Use this [Cookiecutter](https://cookiecutter.readthedocs.io) template to generate
an empty Python package set up with documentation and testing. The project setup
is documented extensively in the [README]({{cookiecutter.project_slug}}/README.md).

How to use
==========
We recommend developing your software in an isolated Python environment. You can
use virualenv + pip or conda.

For example, to create a virtual environment with Python 3, do:
```bash
$ virtualenv -p python3 env
$ . env/bin/activate
```

To do the same using conda, type:
```bash
$ conda create -n env python=3.4
$ source activate env
```

(On windows use `activate env` to activate the conda environment.)

If you don't have cookiecutter installed yet, install it with
```bash
pip install cookiecutter
```

If you use conda, you can also type:
```bash
conda install -c conda-forge cookiecutter
```

To generate the files and directory structure for a new Python project, type:
```bash
cookiecutter https://github.com/nlesc/python-template.git
```

You will be asked to supply the following information about your project:

| Name                      | Default value | Explanation |
| ------------------------- | ------------- | ----------- |
| full_name                 |   | Your full name, e.g. 'John Smith'.   |
| email                     | yourname@esciencecenter.nl | Your (work) email address  |
| code_of_conduct_email     | yourname@esciencecenter.nl | Email address of the person who should be contacted in case of violations of the Code of Conduct.  |
| copyright_holder          |   | Name(s) of the organization(s) or person(s) who hold the copyright of the software (e.g., Netherlands eScience Center).  |
| github_organization       |   | GitHub organization that will contain this project's repository. This can also be your github user name. |
| project_name              | My Python Project  | Full project/package name.  |
| project_slug              | my_python_project  | This will be the name of the directory to be created and the git repository.  |
| project_short_description |   | The information that you enter here will end up in the README, documentation, license, and setup.py, so it may be a good idea to prepare something in advance. |
| version                   | 0.1.0  |   |
| open_source_license       | Apache 2.0 (1)  | The software license under which the code is made available.  |
| apidoc                    | no (1)  | Add support for automatically generating a module index from the `docstrings` in your Python package (look at the [scriptcwl package](http://scriptcwl.readthedocs.io/en/latest/apidocs/scriptcwl.html) for an example). |

How to contribute
=================
Suggestions/improvements/edits are most welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request.
