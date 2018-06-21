{{ cookiecutter.project_name }}
===============================
{{ cookiecutter.project_short_description }}

Project Setup
-------------

Here we provide some details about the project setup. Most of the choices are explained in the guide. Here we list what was done. An example can be found [here](https://github.com/multiscale/muscle3/pull/10/files). Most of this text can be removed once the development of the software package takes off.

### Documentation

* Documentation should be put in the `docs` folder. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
* The `docs/_static` and `docs/_templates` contain an (empty) `.gitignore` file, to be able to add them to the repository. These two files can be safely removed (or you can just leave them there).
* To generate html documentation run `python setup.py build_sphinx`
  - This is configured in `setup.cfg`
  - Alternatively, run `make html` in the `docs` folder.
* We recommend writing the documentation using Restructured Text (reST)
  - [Restructured Text (reST) and Sphinx CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
* To put the documentation on [Read the Docs](https://readthedocs.org), log in to your Read the Docs account, and import the repository (under 'My Projects').

### CITATION.cff

* To allow others to cite your software, add a `CITATION.cff` file
* It only makes sense to do this once there is something to cite (e.g., a software release with a DOI).
* To generate a CITATION.cff file given a DOI, use [doi2cff](https://github.com/citation-file-format/doi2cff).

Documentation
-------------
You could include a link to the full documentation of your project here.

Installation
------------
clone the repository  
    `git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`  
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
Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}

{{ cookiecutter.open_source_license }}

Contributing
------------
Contributing authors so far:
* {{ cookiecutter.full_name }}
