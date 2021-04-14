The file structure of the generated package looks like:

```shell
path/to/package/
├── .editorconfig
└── .github/
    └── workflows
        ├── build.yml
        └── pypi_deploy.yml
├── .gitignore
├── .prospector.yml
├── CHANGELOG.rst
├── CODE_OF_CONDUCT.rst
├── CONTRIBUTING.rst
├── docs
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── LICENSE
├── MANIFEST.in
├── NOTICE
├── package
│   ├── __init__.py
│   ├── __version__.py
│   └── package.py
├── README.rst
├── project_setup.rst
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    ├── test_lint.py
    └── test_package.py
```

* Code (existing or new) should be placed in `path/to/package/package/` (please choose a better name for your software!).
* Add documentation by editing `path/to/package/docs/index.rst`
* Tests go in the `path/to/package/tests/` directory
* The generated [project setup document]({{cookiecutter.project_name}}/project_setup.md) contains extensive documentation about the project setup and provides further instructions on what to do.

### Step 3: Create and activate a Python environment

* If you are using **virtualenv + pip3**, do:
     ```bash
     $ virtualenv -p python3 env
     $ . env/bin/activate
     ```
* If you are using **conda**, type:
    ```bash
    $ conda create -n env python=3
    $ source activate env
    ```
    (On windows use `activate env` to activate the conda environment.)

## Continuous integration with Github Actions

The template has two Ci workflows. They can be found in **.github/workflows** folder.

1. **build.yml**

This workflow install the dependencies, builds the package and runs tests.

2. **pypi.yml**

This workflow pushes the package to [PYPI](https://pypi.org/). This action will require PYPI token to be stored as [Github secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets). The workflow uses secret with a name of `PYPI_TOKEN`.

You can learn more about Python packaging at [this link](https://packaging.python.org/tutorials/packaging-projects/).
