################################################################################
{{ cookiecutter.project_name }}
################################################################################

{{ cookiecutter.project_short_description }}

Project Setup
*************

Here we provide some details about the project setup. Most of the choices are explained in the `guide <https://guide.esciencecenter.nl>`_. Links to the relevant sections are included below.
Feel free to remove this text when the development of the software package takes off.

For a quick reference on software development, we refer to `the software guide checklist <https://guide.esciencecenter.nl/best_practices/checklist.html>`_.

Version control
---------------

Once your Python package is created, put it under
`version control <https://guide.esciencecenter.nl/best_practices/version_control.html>`_!
We recommend using `git <http://git-scm.com/>`_ and `github <https://github.com/>`_.

.. code-block:: console

  cd {{ cookiecutter.project_slug }}
  git init
  git add -A
  git commit

To put your code on github, follow `this tutorial <https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/>`_.

Python versions
---------------

This repository is set up with Python versions:

{%- if cookiecutter.Python_version == 'Python 2 and 3' or cookiecutter.Python_version == 'Python 2' %}
* 2.7
{%- endif %}
{%- if cookiecutter.Python_version == 'Python 3' or cookiecutter.Python_version == 'Python 2 and 3' %}
* 3.4
* 3.5
* 3.6
{%- endif %}

Add or remove Python versions based on project requirements. `The guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html>`_ contains more information about Python versions and writing Python 2 and 3 compatible code.

Package management and dependencies
-----------------------------------

You can use either `pip` or `conda` for installing dependencies and package management. This repository does not force you to use one or the other, as project requirements differ. For advice on what to use, please check `the relevant section of the guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#dependencies-and-package-management>`_.

* Dependencies should be added to `setup.py` in the `install_requires` list.

Packaging/One command install
-----------------------------

You can distribute your code using pipy or conda. Again, the project template does not enforce the use of either one. `The guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#building-and-packaging-code>`_ can help you decide which tool to use for packaging.

Testing and code coverage
-------------------------

* Tests should be put in the ``tests`` folder.
* The testing framework used is `PyTest <https://pytest.org>`_

  - `PyTest introduction <http://pythontesting.net/framework/pytest/pytest-introduction/>`_

* Tests can be run with ``python setup.py test``

  - This is configured in ``setup.py`` and ``setup.cfg``

* Use `Travis CI <https://travis-ci.com/>`_ to automatically run tests and to test using multiple Python versions

  - Configuration can be found in ``.travis.yml``
  - `Getting started with Travis CI <https://docs.travis-ci.com/user/getting-started/>`_

* TODO: add something about code quality/coverage tool?
* `Relevant section in the guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#testing>`_

Documentation
-------------

* Documentation should be put in the ``docs`` folder. The contents have been generated using ``sphinx-quickstart`` (Sphinx version 1.6.5).
* We recommend writing the documentation using Restructured Text (reST) and Google style docstrings.

  - `Restructured Text (reST) and Sphinx CheatSheet <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_
  - `Google style docstring examples <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.

* To generate html documentation run ``python setup.py build_sphinx``

  - This is configured in ``setup.cfg``
  - Alternatively, run ``make html`` in the ``docs`` folder.

* The ``docs/_static`` and ``docs/_templates`` contain an (empty) ``.gitignore`` file, to be able to add them to the repository. These two files can be safely removed (or you can just leave them there).
* To put the documentation on `Read the Docs <https://readthedocs.org>`_, log in to your Read the Docs account, and import the repository (under 'My Projects').

  - Include the link to the documentation in this README_.

* `Relevant section in the guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#writingdocumentation>`_

Coding style conventions and code quality
-----------------------------------------

* Check your code style with ``prospector``
* You may need run ``pip install .[dev]`` first, to install the required dependencies
* You can use ``yapf`` to fix the readability of your code style and ``isort`` to format and group your imports
* `Relevant section in the guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#coding-style-conventions>`_

CHANGELOG.rst
-------------

* Document changes to your software package
* `Relevant section in the guide <https://guide.esciencecenter.nl/software/releases.html#changelogmd>`_

CITATION.cff
------------

* To allow others to cite your software, add a ``CITATION.cff`` file
* It only makes sense to do this once there is something to cite (e.g., a software release with a DOI).
* To generate a CITATION.cff file given a DOI, use `doi2cff <https://github.com/citation-file-format/doi2cff>`_.
* `Relevant section in the guide <https://guide.esciencecenter.nl/software/documentation.html#citation-file>`_

CODE_OF_CONDUCT.rst
-------------------

* Information about how to behave professionally
* `Relevant section in the guide <https://guide.esciencecenter.nl/software/documentation.html#code-of-conduct>`_

CONTRIBUTING.rst
----------------

* Information about how to contribute to this software package
* `Relevant section in the guide <https://guide.esciencecenter.nl/software/documentation.html#contribution-guidelines>`_

MANIFEST.in
-----------

* List non-Python files that should be included in a source distribution
* `Relevant section in the guide <https://guide.esciencecenter.nl/best_practices/language_guides/python.html#building-and-packaging-code>`_

NOTICE
------

* List of attributions of this project and Apache-license dependencies
* `Relevant section in the guide <https://guide.esciencecenter.nl/best_practices/licensing.html#notice>`_

Installation
------------

To install {{ cookiecutter.project_slug }}, do:

.. code-block:: console

  git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
  cd {{ cookiecutter.project_slug }}
  pip install .


Run tests (including coverage) with:

.. code-block:: console

  python setup.py test


Documentation
*************

.. _README:

Include a link to your project's full documentation here.

Contributing
************

If you want to contribute to the development of {{ cookiecutter.project_name }},
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

License
*******

Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.copyright_holder }}
{% if cookiecutter.open_source_license == 'MIT license' %}
Licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
{% elif cookiecutter.open_source_license == 'BSD license' %}
Licensed under the 3-clause BSD License.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

* Neither the name of {{ cookiecutter.copyright_holder }} nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
{% elif cookiecutter.open_source_license == 'ISC license' %}
Licensed under the ISC License.

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
{% elif cookiecutter.open_source_license == 'Apache Software License 2.0' %}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

{% elif cookiecutter.open_source_license == 'GNU General Public License v3 or later' %}
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
{% endif %}

Credits
*******

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
