{{ cookiecutter.project_name }}
===============================
{{ cookiecutter.project_short_description }}

Project Setup
-------------

Here we provide some details about the project setup. Most of the choices are explained in the [guide](https://guide.esciencecenter.nl). Links to the relevant sections are included below. Most of this text can be removed once the development of the software package takes off.

For a quick reference on software development, we refer to [the software guide checklist](https://guide.esciencecenter.nl/software/checklist.html).

### Version control

Once your Python package is created, put it under version control!

```
cd {{ cookiecutter.project_slug }}
git init
git add -A
git commit
```

### Python versions

This repository is set up with Python versions: 2.7, 3.4, 3.5, and 3.6. Add or remove Python versions based on project requirements. [The guide](https://guide.esciencecenter.nl/languages/python.html) contains more information about Python versions and writing Python 2 and 3 compatible code.

### Package management

You can use either `pip` or `conda` for installing dependencies and package management. This repository does not force you to use one or the other, as project requirements differ. For advice on what to use, please check [the relevant section of the guide](https://guide.esciencecenter.nl/languages/python.html#dependencies-and-package-management).

### Packaging/One command install

You can distribute your code using pipy or conda. Again, the project template does not enforce the use of either one. [The guide](https://guide.esciencecenter.nl/languages/python.html#building-and-packaging-code) can help you decide which tool to use for packaging.

### Testing and code coverage

* Tests should be put in the `tests` folder.
* The testing framework used is [PyTest](https://pytest.org)
  - [PyTest introduction](http://pythontesting.net/framework/pytest/pytest-introduction/)
* Tests can be run with `python setup.py test`
  - This is configured in `setup.py` and `setup.cfg`
* Use [Travis CI](https://travis-ci.com/) to automatically run tests and to test using multiple Python versions
  - Configuration can be found in `.travis.yml`
  - [Getting started with Travis CI](https://docs.travis-ci.com/user/getting-started/)
* TODO: add something about code quality/coverage tool?

### Documentation

* Documentation should be put in the `docs` folder. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
* The `docs/_static` and `docs/_templates` contain an (empty) `.gitignore` file, to be able to add them to the repository. These two files can be safely removed (or you can just leave them there).
* To generate html documentation run `python setup.py build_sphinx`
  - This is configured in `setup.cfg`
  - Alternatively, run `make html` in the `docs` folder.
* We recommend writing the documentation using Restructured Text (reST)
  - [Restructured Text (reST) and Sphinx CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
* To put the documentation on [Read the Docs](https://readthedocs.org), log in to your Read the Docs account, and import the repository (under 'My Projects').

### Coding style conventions and code quality

* Check your code style with `prospector`
* You may need run `pip install {{ cookiecutter.project_slug }}[dev]` first, to install the required dependencies
* You can use `yapf` to fix the readability of your code style and `isort` to format and group your imports
* [Relevant section in the guide](https://guide.esciencecenter.nl/languages/python.html#coding-style-conventions)

### CHANGELOG.md

* Document changes to your software package
* [Relevant section in the guide](https://guide.esciencecenter.nl/software/releases.html#changelogmd)

### CITATION.cff

* To allow others to cite your software, add a `CITATION.cff` file
* It only makes sense to do this once there is something to cite (e.g., a software release with a DOI).
* To generate a CITATION.cff file given a DOI, use [doi2cff](https://github.com/citation-file-format/doi2cff).
* * [Relevant section in the guide](https://guide.esciencecenter.nl/software/documentation.html#citation-file)

### CODE_OF_CONDUCT.md

* Information about how to behave professionally
* [Relevant section in the guide](https://guide.esciencecenter.nl/software/documentation.html#code-of-conduct)
*
### CONTRIBUTING.md

* Information about how to contribute to this software package
* [Relevant section in the guide](https://guide.esciencecenter.nl/software/documentation.html#contribution-guidelines)

### MANIFEST.in

* List non-Python files that should be included in a source distribution
* [Relevant section in the guide](https://guide.esciencecenter.nl/languages/python.html#building-and-packaging-code)

### NOTICE

* List of licenses of the project and dependencies
* [Relevant section in the guide](https://guide.esciencecenter.nl/software/licensing.html#noticetxtmd)

Documentation
-------------
You could include a link to the full documentation of your project here.

Installation
------------
clone the repository  
    `git clone git@github.com:{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git`
change into the top-level directory  
    `cd {{ cookiecutter.project_slug }}`  
install using  
    `pip install .`

Run tests (including coverage) with:
```
python setup.py test
```

Check code style using:
```
prospector
```
(You may need to `pip install prospector[with_pyroma]` first.)

To automatically fix code style errors, run `yapf -i yourfile.py`.
Run `yapf -d yourfile.py` to preview what would be changed.
Run `pip install --upgrade yapf` to install the latest version of yapf.

Dependencies
------------
 * Python 2.7 or Python 3.5

License
-------
Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.copyright_holder }}

{{ cookiecutter.open_source_license }}

Contributing
------------
Contributing authors so far:
* {{ cookiecutter.full_name }}
