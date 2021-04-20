``{{ cookiecutter.package_name }}`` developer documentation
=====================================

If you're looking for user documentation, go `here <README.rst>`_.

|
|

Development install
-------------------

.. code:: shell

    # Create a virtualenv, e.g. with
    python3 -m venv env

    # activate virtualenv
    source env/bin/activate
    
    # make sure to have a recent version of pip and setuptools
    pip install --upgrade pip setuptools

    # (from the project root directory)
    # install {{ cookiecutter.package_name }} as an editable package
    pip install --no-cache-dir --editable .
    # install development dependencies
    pip install --no-cache-dir --editable .[dev]

Afterwards check that the install directory is present in the ``PATH``
environment variable.

Running the tests
-----------------

Running the tests requires an activated virtualenv with the development tools installed.

.. code:: shell

    # unit tests
    pytest
    pytest tests/
    
Running linters locally
-----------------------

Running the linters requires an activated virtualenv with the development tools installed.

.. code:: shell

    # linter
    prospector

    # recursively check import style for the {{ cookiecutter.package_name }} module only
    isort --recursive --check-only {{ cookiecutter.package_name }}

    # recursively check import style for the {{ cookiecutter.package_name }} module only and show
    # any proposed changes as a diff
    isort --recursive --check-only --diff {{ cookiecutter.package_name }}

    # recursively fix  import style for the {{ cookiecutter.package_name }} module only
    isort --recursive {{ cookiecutter.package_name }}

You can enable automatic linting with ``prospector`` and ``isort`` on commit by enabling the git hook from
``.githooks/pre-commit``, like so:

.. code:: shell

    git config --local core.hooksPath .githooks

Versioning
----------

Bumping the version across all files is done with bump2version, e.g.

.. code:: shell

    bump2version major
    bump2version minor
    bump2version patch

Making a release
----------------

Preparation
^^^^^^^^^^^

1. Update the ``CHANGELOG.md``
2. Verify that the information in ``CITATION.cff`` is correct, and that ``.zenodo.json`` contains equivalent data
3. Make sure the version has been updated.
4. Run the unit tests with ``pytest tests/``

PyPI
^^^^

In a new terminal, without an activated virtual environment or an `env` directory:

.. code:: shell

    # prepare a new directory
    cd $(mktemp -d --tmpdir {{ cookiecutter.package_name }}.XXXXXX)
    
    # fresh git clone ensures the release has the state of origin/main branch
    git clone {{ cookiecutter.repository }} .
    
    # prepare a clean virtual environment and activate it
    python3 -m venv env
    source env/bin/activate
    
    # make sure to have a recent version of pip and setuptools
    pip install --upgrade pip setuptools

    # install runtime dependencies and publishing dependencies
    pip install --no-cache-dir .
    pip install --no-cache-dir .[publishing]
    
    # clean up any previously generated artefacts 
    rm -rf {{ cookiecutter.package_name }}.egg-info
    rm -rf dist
    
    # create the source distribution and the wheel
    python setup.py sdist bdist_wheel

    # upload to test pypi instance (requires credentials)
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Keep the terminal open, we'll need it later.

In a new terminal, without an activated virtual environment or an `env` directory:

.. code:: shell
    
    cd $(mktemp -d --tmpdir {{ cookiecutter.package_name }}-test.XXXXXX)

    # prepare a clean virtual environment and activate it
    python3 -m venv env
    source env/bin/activate
    
    # make sure to have a recent version of pip and setuptools
    pip install --upgrade pip setuptools

    # install in user space from test pypi instance:
    python3 -m pip -v install --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple {{ cookiecutter.package_name }}

Check that the package works as it should when installed from pypitest.

Then upload to pypi.org with:

.. code:: shell

    # Back to the first terminal,
    # FINAL STEP: upload to PyPI (requires credentials)
    twine upload dist/*

GitHub
^^^^^^

Don't forget to also make a release on GitHub. If your repository uses the GitHub-Zenodo integration this will also
trigger Zenodo into making a snapshot of your repository and sticking a DOI on it. 
