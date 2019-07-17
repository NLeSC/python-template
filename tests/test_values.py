import pytest
import os
import sys

try:
    import sh
except ImportError:
    pass


@pytest.mark.skipif(sys.platform.startswith('win'),
                    reason='Skipping test with sh-module on Windows')
def test_double_quotes_in_name_and_description(cookies):
    ctx = {'project_short_description': '"double quotes"',
           'full_name': '"name"name'}
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0

    with open(os.path.join(str(project.project), 'setup.py')) as f:
        setup = f.read()
    print(setup)

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'install'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


@pytest.mark.skipif(sys.platform.startswith('win'),
                    reason='Skipping test with sh-module on Windows')
def test_single_quotes_in_name_and_description(cookies):
    ctx = {'project_short_description': "'single quotes'",
           'full_name': "Mr. O'Keeffe"}
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0

    with open(os.path.join(str(project.project), 'setup.py')) as f:
        setup = f.read()
    print(setup)

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'install'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


@pytest.mark.skipif(sys.platform.startswith('win'),
                    reason='Skipping test with sh-module on Windows')
def test_dash_in_project_slug(cookies):
    ctx = {'project_slug': "my-package"}
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0

    with open(os.path.join(str(project.project), 'setup.py')) as f:
        setup = f.read()
    print(setup)

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'install'])
        sh.python(['setup.py', 'build_sphinx'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)


@pytest.mark.skipif(sys.platform.startswith('win'),
                    reason='Skipping test with sh-module on Windows')
def test_space_in_project_slug(cookies):
    ctx = {'project_slug': "my package"}
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0

    with open(os.path.join(str(project.project), 'setup.py')) as f:
        setup = f.read()
    print(setup)

    cwd = os.getcwd()
    os.chdir(str(project.project))

    try:
        sh.python(['setup.py', 'install'])
        sh.python(['setup.py', 'build_sphinx'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)
