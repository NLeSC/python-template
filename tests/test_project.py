import pytest
import sh
import os
import sys

from ruamel import yaml

def load_yaml(filename):
    """Return object in yaml file."""
    with open(filename) as myfile:
        content = myfile.read()
        if "win" in sys.platform:
            content = content.replace("\\", "/")
        return yaml.safe_load(content)

def test_project(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename == 'my_python_project'
    assert project.project.isdir()


def test_install(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'install'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


def test_running_tests(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'test'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


def test_building_documentation_no_apidocs(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'build_sphinx'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


def test_building_documentation_apidocs(cookies):
    project = cookies.bake(extra_context={'apidoc': 'yes'})

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'build_sphinx'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)

    apidocs = project.project.join('docs', '_build', 'html', 'apidocs')

    assert apidocs.join('my_python_project.html').isfile()
    assert apidocs.join('my_python_project.my_python_project.html').isfile()

def test_no_travis_pypi_deployment(cookies):
    project = cookies.bake(extra_context={'apidoc': 'yes'})

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    conf = load_yaml('.travis.yml')

    assert conf.get('deploy') is None


def test_no_travis_pypi_deployment(cookies):
    project = cookies.bake(extra_context={'pypi_user': 'user'})

    assert project.exit_code == 0
    assert project.exception is None

    cwd = os.getcwd()
    os.chdir(str(project.project))

    conf = load_yaml('.travis.yml')

    assert conf.get('deploy').get('user') == 'user'
