{{ cookiecutter.project_name }}
===============================
{{ cookiecutter.project_short_description }}

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
