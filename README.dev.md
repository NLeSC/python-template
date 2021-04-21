# Netherlands eScience Center Python Template - developer documentation

If you're looking for user documentation, go [here](README.md).

## Development install

```shell
# Create a virtual environment, e.g. with
python3 -m venv env

# activate virtual environment
source env/bin/activate

# make sure to have a recent version of pip and setuptools
pip install --upgrade pip setuptools

# (from the project root directory)
# install {{ cookiecutter.package_name }} as an editable package
pip install --no-cache-dir --editable .
# install development dependencies
pip install --no-cache-dir --editable .[dev]
```

Afterwards check that the install directory is present in the `PATH` environment variable.

## Running the tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# unit tests
pytest
pytest tests/
```

## Making a release

### Preparation

1.  Update the `CHANGELOG.md`
2.  Verify that the information in `CITATION.cff` is correct, and that `.zenodo.json` contains equivalent data
3.  Make sure the version has been updated.
4.  Run the unit tests with `pytest tests/`

### GitHub

If your repository uses the GitHub-Zenodo integration this will also
trigger Zenodo into making a snapshot of your repository and sticking a DOI on it.
