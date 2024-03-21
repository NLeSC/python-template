# `{{ cookiecutter.package_name }}` developer documentation

If you're looking for user documentation, go [here](README.md).

## Development install

```shell
# Create a virtual environment, e.g. with
python -m venv env

# activate virtual environment
source env/bin/activate

# make sure to have a recent version of pip and setuptools
python -m pip install --upgrade pip setuptools

# (from the project root directory)
# install {{ cookiecutter.package_name }} as an editable package
python -m pip install --no-cache-dir --editable .
# install development dependencies
python -m pip install --no-cache-dir --editable .[dev]
```

Afterwards check that the install directory is present in the `PATH` environment variable.

## Running the tests

There are two ways to run tests.

The first way requires an activated virtual environment with the development tools installed:

```shell
pytest -v
```

The second is to use `tox`, which can be installed separately (e.g. with `pip install tox`), i.e. not necessarily inside the virtual environment you use for installing `{{ cookiecutter.package_name }}`, but then builds the necessary virtual environments itself by simply running:

```shell
tox
```

Testing with `tox` allows for keeping the testing environment separate from your development environment.
The development environment will typically accumulate (old) packages during development that interfere with testing; this problem is avoided by testing with `tox`.

### Test coverage

In addition to just running the tests to see if they pass, they can be used for coverage statistics, i.e. to determine how much of the package's code is actually executed during tests.
In an activated virtual environment with the development tools installed, inside the package directory, run:

```shell
coverage run
```

This runs tests and stores the result in a `.coverage` file.
To see the results on the command line, run

```shell
coverage report
```

`coverage` can also generate output in HTML and other formats; see `coverage help` for more information.

## Running linters locally

For linting and sorting imports we will use [ruff](https://beta.ruff.rs/docs/). Running the linters requires an 
activated virtual environment with the development tools installed.

```shell
# linter
ruff .

# linter with automatic fixing
ruff . --fix
```

To fix readability of your code style you can use [yapf](https://github.com/google/yapf).

You can enable automatic linting with `ruff` on commit by enabling the git hook from `.githooks/pre-commit`, like so:

```shell
git config --local core.hooksPath .githooks
```

## Generating the API docs

```shell
cd docs
make html
```

The documentation will be in `docs/_build/html`

If you do not have `make` use

```shell
sphinx-build -b html docs docs/_build/html
```

To find undocumented Python objects run

```shell
cd docs
make coverage
cat _build/coverage/python.txt
```

To [test snippets](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) in documentation run

```shell
cd docs
make doctest
```

## Versioning

Bumping the version across all files is done with [bump-my-version](https://github.com/callowayproject/bump-my-version), e.g.

```shell
bump-my-version major  # bumps from e.g. 0.3.2 to 1.0.0
bump-my-version minor  # bumps from e.g. 0.3.2 to 0.4.0
bump-my-version patch  # bumps from e.g. 0.3.2 to 0.3.3
```

## Using Github Actions to make a release of the package

This section describes how to make a release with a GitHub actions workflow.

### Setup 
The following steps set up the infrastructure for making releases easy via Github Actions. They are necessary once for your package.


#### (1/2) Define Github workflow

This is necessary once per package.

You can set up a workflow file following instructions [here](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/). 
The workflow consists of 3 jobs: build, publishing to testpypi, publishing to pypi. The workflow for build is as usual.

The job for publishing on TestPyPI is as follows:

```yml
publish-to-testpypi:
    name: Publish Python distribution to TestPyPI
    needs:
    - build
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest

    environment:
        name: testpypi
        url: https://test.pypi.org/p/{{ cookiecutter.package_name }}

    permissions:
        id-token: write  # IMPORTANT: mandatory for trusted publishing

    steps:
    - name: Download all the dists
        uses: actions/download-artifact@v3
        with:
        name: python-package-distributions
        path: dist/
    - name: Publish distribution to TestPyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
        repository-url: https://test.pypi.org/legacy/
        verbose: true # optional; for debugging
```


The job for publishing on PyPI is as follows:

```yml
publish-to-pypi:
    name: >-
        Publish Python distribution to PyPI
    if: github.event_name == 'release' && github.event.action == 'published'
    needs:
    - build
    runs-on: ubuntu-latest
    environment:
        name: pypi
        url: https://pypi.org/p/{{ cookiecutter.package_name }} 
    permissions:
        id-token: write  # IMPORTANT: mandatory for trusted publishing

    steps:
    - name: Download all the dists
        uses: actions/download-artifact@v3
        with:
        name: python-package-distributions
        path: dist/
    - name: Publish distribution to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
        verbose: true

```

Notes
- The `id-token: write` item is important because it will enable GitHub to publish your package on PyPI (see below). You can read more about how this works [here](https://docs.pypi.org/trusted-publishers/).
- The `url` item for `environment` needs to match exactly the PyPI projecte name, defined in the next step.

#### (2/2) PyPI and TestPyPI

This is necessary once per package. 

On your TestPyPI account, go to "Your Projects", and  under "Publishing", fill the form for "Add a new pending publisher". You need to specify:
- {{ cookiecutter.package_name }} as the PyPI project name. 
- The workflow name as the name of the `yml` file with the github workflow, for instance `release.yml`
- The environment name as defined in the workflow file, in the above examples this is `testpypi` and `pypi`

Do the same on your PyPI account. 


### Making a release 

With the described setup, you can now make a new release in 3 steps.

#### (1/3) Preparation

1. Update the <CHANGELOG.md> (don't forget to update links at bottom of page)
2. Verify that the information in [`CITATION.cff`](CITATION.cff) is correct.
3. Make sure the [version has been updated](#versioning).
4. Run the unit tests with `pytest -v`


#### (2/3) Make a release to TestPyPI

In your web browser, visit [{{cookiecutter.repository}}/actions/workflows/release.yml]({{cookiecutter.repository}}/actions/workflows/release.yml). Click on "Run workflow".

If the workflow passes, you have successfully released a new version to TestPyPI. Verify this by visiting [https://test.pypi.org/project/{{cookiecutter.package_name}}](https://test.pypi.org/project/{{cookiecutter.package_name}})

If the workflow fails, you should investigate the bug. You can use a [manual upload with twine](https://docs.pypi.org/trusted-publishers/using-a-publisher/#the-manual-way) for this.

#### (3/3) Make a release on Github, triggering a release to PyPI

If the release to TestPyPI worked, you can now release to PyPI. 
Visit [{{cookiecutter.repository}}/releases/new]({{cookiecutter.repository}}/releases/new) and make a new release. When this is done, the github action workflow defined above runs. You can check that the workflow ran correctly, and visit [https://test.pypi.org/project/{{cookiecutter.package_name}}](https://test.pypi.org/project/{{cookiecutter.package_name}}) to make sure the release is on PyPI.
If your repository uses the GitHub-Zenodo integration this will also trigger Zenodo into making a snapshot of your repository and sticking a DOI on it.