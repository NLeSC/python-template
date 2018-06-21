NLeSC Cookiecutter template for Python
======================================

This repository can be used to create empty Python projects for newly
started Python projects within the Netherlands eScience Center, being
compliant for as much as possible with the [Software Development Guide](https://guide.esciencecenter.nl/).

This repository is intended for use with cookiecutter. Cookiecutter is a
command-line utility that creates projects from project templates. For
more information about cookiecutter checkout
<https://cookiecutter.readthedocs.io>.

We've tried to keep the template as minimal as possible for now, to
prevent having to delete a lot of clutter after creating an empty
project, but if you feel something essential is missing let us know.


How to use
==========
The easiest way to develop for python is to setup a virtual environment for your project; we also recommend using python3:
```bash
$ virtualenv -p python3 env
$ . env/bin/activate
```

If you don't have cookiecutter installed yet, use  
    `pip install cookiecutter`  
to install cookiecutter.

Once cookiecutter is installed you can use  
    `cookiecutter https://github.com/benvanwerkhoven/cookie-python.git`  
to create a new Python project.

After this command you will be prompted with a number of questions. This information will be used to fill out the
template as the new project directory structure is created for you. Below is a short explanation of what exactly will be asked from you.

 * *full_name []:* Please fill in your full name. e.g. 'John Smith'
 * *email [yourname@esciencecenter.nl]:* Your work email adress
 * *coc_email [yourname@esciencecenter.nl]:* Email address of the person who should be contacted in case of violations of the Code of Conduct (could be the PI)
 * *github_username []:* Please enter the GitHub username that will be the owner of the repository for this project.
 * *project_name [Python Boilerplate]:* Please write the name of your project out in full.
 * *project_slug []:* This will be the name of the directory to be created and the git repository.
 * *project_short_description []:* The information that you enter here will end up in the README.md, the License and the setup.py files, so it may be a good idea to have a short description of the project ready.
 * *version [0.1.0]:* The first version for your project, NLeSC preference is using semantic versioning
 * *Select open_source_license:* The intended license, NLeSC preference is Apache 2.0  


How to contribute
=================
Suggestions/improvements/edits are most welcome. You can create a pull
request if you like or just send Carlos or Ben an email.

Contributing authors so far:
 * Carlos Martinez Ortiz
 * Ben van Werkhoven
 * Jisk Attema
