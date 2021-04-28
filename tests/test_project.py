import os
import subprocess
from sys import platform


def test_project_folder(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename == 'my-python-project'
    assert project.project.isdir()


def run(command: str, dirpath: os.PathLike) -> subprocess.CompletedProcess:
    print(command.split(' '))
    return subprocess.run(command.split(' '),
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          cwd=dirpath,
                          encoding='utf-8')


def test_pytest(cookies):
    env_bin = 'env/Scripts/' if platform.startswith("win") else 'env/bin/'
    result = cookies.bake()
    env_output = run(f'python3 -m venv env', result.project)
    print(env_output.stdout)
    print(env_output.stderr)
    assert env_output.returncode == 0
    latest_pip_output = run(f'{env_bin}pip3 install --upgrade pip setuptools', result.project)
    assert latest_pip_output.returncode == 0
    pip_output = run(f'{env_bin}pip3 install --editable .[dev]', result.project)
    assert pip_output.returncode == 0

    pytest_output = run(f'{env_bin}pytest', result.project)
    assert pytest_output.returncode == 0
    assert '== 3 passed in' in  pytest_output.stdout
    assert (result.project / 'coverage.xml').exists()
    assert (result.project / 'htmlcov/index.html').exists()
