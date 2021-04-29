import os
import subprocess
from sys import platform
from typing import Sequence

import pytest


def test_project_folder(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename == 'my-python-project'
    assert project.project.isdir()


def run(args: Sequence[str], dirpath: os.PathLike) -> subprocess.CompletedProcess:
    return subprocess.run(args=args,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          cwd=dirpath,
                          encoding="utf-8")


@pytest.fixture
def baked_withdevdeps(cookies):
    result = cookies.bake()
    env_output = run(['python3', '-m', 'venv', 'env'], result.project)
    assert env_output.returncode == 0
    env_bin = 'env/Scripts/' if platform.startswith("win") else 'env/bin/'
    latest_pip_output = run([f'{env_bin}pip3', 'install', '--upgrade', 'pip', 'setuptools'], result.project)
    assert latest_pip_output.returncode == 0
    pip_output = run([f'{env_bin}pip3', 'install', '--editable', '.[dev]'], result.project)
    assert pip_output.returncode == 0
    return result.project, env_bin


def test_pytest(baked_withdevdeps):
    project_dir, env_bin = baked_withdevdeps
    pytest_output = run([f'{env_bin}pytest'], result.project)
    assert pytest_output.returncode == 0
    assert '== 3 passed in' in pytest_output.stdout
    assert (project_dir / 'coverage.xml').exists()
    assert (project_dir / 'htmlcov/index.html').exists()


def test_subpackage(baked_withdevdeps):
    project_dir, env_bin = baked_withdevdeps
    subpackage = (project_dir / 'my_python_package' / 'mysub')
    subpackage.mkdir()
    (subpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    subsubpackage = (project_dir / 'my_python_package' / 'mysub' / 'mysub2')
    subsubpackage.mkdir()
    (subsubpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    build_output = run([f'{env_bin}python3', 'setup.py', 'build'], project_dir)
    assert build_output.returncode == 0
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / '__init__.py').exists()
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / 'mysub2' / '__init__.py').exists()
