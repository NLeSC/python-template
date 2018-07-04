Netherlands eScience Center Python Template
===========================================

Spend less time setting up and configuring your new Python projects and comply with the
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

* *full_name []:* Please fill in your full name. e.g. 'John Smith'
* *email [yourname@esciencecenter.nl]:* Your work email address
* *code_of_conduct_email [yourname@esciencecenter.nl]:* Email address of the person who should be contacted in case of violations of the Code of Conduct (could be the PI)
* *copyright_holder:* Name(s) of the organization(s) or person(s) who hold the copyright of the software (e.g., Netherlands eScience Center)
* *github_organization []:* Please enter the GitHub organization that will contain this project's repository. This can also be your github user name.
* *project_name [Python Boilerplate]:* Please write the name of your project out in full.
* *project_slug []:* This will be the name of the directory to be created and the git repository.
* *project_short_description []:* The information that you enter here will end up in the README.md, the License and the setup.py files, so it may be a good idea to have a short description of the project ready.
* *version [0.1.0]:* The first version for your project, NLeSC preference is using semantic versioning
* *Select open_source_license:* The intended license, NLeSC preference is Apache 2.0
* *apidoc:* Add support for automatically generating a module index from the `docstrings` in your Python package (look at the [scriptcwl package](http://scriptcwl.readthedocs.io/en/latest/apidocs/scriptcwl.html) for an example); the default is no apidocs

How to contribute
=================
Suggestions/improvements/edits are most welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request.
