import os
import subprocess
import shlex


def test_project_folder(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename == 'my-python-project'
    assert project.project.isdir()


def run(command: str, dirpath: os.PathLike) -> subprocess.CompletedProcess:
    return subprocess.run(shlex.split(command),
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          cwd=dirpath,
                          universal_newlines=True)


def test_pytest(cookies):
    result = cookies.bake()
    env_output = run('python3 -m venv env', result.project)
    assert env_output.returncode == 0
    latest_pip_output = run('env/bin/pip3 install --upgrade pip setuptools', result.project)
    assert latest_pip_output.returncode == 0
    pip_output = run('env/bin/pip3 install --editable .[dev]', result.project)
    assert pip_output.returncode == 0

    pytest_output = run('env/bin/pytest', result.project)
    assert pytest_output.returncode == 0
    assert '== 3 passed in' in  pytest_output.stdout
    assert (result.project / 'coverage.xml').exists()
    assert (result.project / 'htmlcov/index.html').exists()
