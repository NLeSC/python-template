# Developer documentation

If you're looking for user documentation, go [here](README.md).

## Development install

### Install `cookiecutter` in user space

We recommend installing `cookiecutter` in user space as per `cookiecutter`'s instructions. This way, you don't have to
install `cookiecutter` for every new project.

```shell
python3 -m pip install --user --upgrade cookiecutter
```

### Get your own copy of the repository

Before you can do development work on the template, you'll need to check out a local copy of the repository:

```shell
cd <where you keep your GitHub repositories>
git clone https://github.com/NLeSC/python-template.git
cd python-template
```

### Create a virtual environment

Next, make a virtual environment, activate it, and install the development dependencies in it. This will enable you to 
run the tests later.

```shell
# Create a virtual environment, e.g. with
python3 -m venv env

# activate virtual environment
source env/bin/activate

# make sure to have a recent version of pip and setuptools
python3 -m pip install --upgrade pip setuptools

# (from the project root directory)
# install development dependencies
python3 -m pip install --no-cache-dir .[dev]
```

## Running the tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# unit tests
pytest
pytest tests/
```

## Using `cookiecutter` to generate a new package from the command line

While making changes to the template, you'll regularly want to verify that the packages generated with the template
still work. Any easy way to do this is to generate new packages in a temporary directory (which will get removed
everytime you reboot), for example like so:

```shell
# change directory to a new temporary directory
cd $(mktemp -d --tmpdir cookiecutter-generated.XXXXXX)

# run cookiecutter with the template to generate a new package
cookiecutter <path to where your template is>

# when it asks you for the GitHub organization, put in your own name;
# for the other questions, just accept the default

# 'ls' should return just the one directory called 'my-python-project'
ls 
```

If your Python package was created successfully, `cookiecutter` will point you to a file
(`my-python-project/README.next_steps.md`) that contains information on next steps.

In addition to the information in `my-python-project/README.project_layout_explained.md`, the developer documentation
`my-python-project/README.dev.md` contains information on a few more things to check, for example:

1. generating `my-python-project`'s documentation locally
1. running `my-python-project`'s tests locally
1. running `my-python-project`'s linters locally
1. verifying that the `my-python-project`'s version can be updated using `bumpversion`
1. making a release of `my-python-project` on https://test.pypi.org/

Follow the instructions from `my-python-project/README.dev.md` and make sure that everything works.

## Making a release

### Preparation

1. Make sure the `CHANGELOG.md` has been updated
2. Verify that the information in `CITATION.cff` is correct, and that `.zenodo.json` contains equivalent data
3. Make sure that `version` in [setup.cfg](setup.cfg) and  `version` in [CITATION.cff](CITATION.cff) have been bumped to the to-be-released version of the template
4. Run the unit tests with `pytest tests/`
5. Go through the steps outlined above for [generating a new package from the command line](#using-cookiecutter-to-generate-a-new-package-from-the-command-line), and verify that the generated package works as it should.

### GitHub

1. Make sure that the GitHub-Zenodo integration is enabled for https://github.com/NLeSC/python-template
1. Go to https://github.com/NLeSC/python-template/releases and click `Draft a new release`
