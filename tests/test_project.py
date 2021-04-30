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


def run(args: Sequence[str], dirpath: os.PathLike, env_bin=None) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    if env_bin:
        env['PATH'] = os.getcwd() + env_bin + ':' + os.environ.get('PATH')
    return subprocess.run(args=args,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          cwd=dirpath,
                          env=env,
                          encoding="utf-8")


@pytest.fixture
def baked_with_development_dependencies(cookies):
    result = cookies.bake()
    env_output = run(['python3', '-m', 'venv', 'env'], result.project)
    assert env_output.returncode == 0
    env_bin = 'env/Scripts/' if platform.startswith("win") else 'env/bin/'
    latest_pip_output = run(['pip3', 'install', '--upgrade', 'pip', 'setuptools'], result.project, env_bin)
    assert latest_pip_output.returncode == 0
    pip_output = run(['pip3', 'install', '--editable', '.[dev]'], result.project, env_bin)
    assert pip_output.returncode == 0
    return result.project, env_bin


def test_pytest(baked_with_development_dependencies):
    project_dir, env_bin = baked_with_development_dependencies
    pytest_output = run(['pytest'], project_dir, env_bin)
    assert pytest_output.returncode == 0
    assert '== 3 passed in' in pytest_output.stdout
    assert (project_dir / 'coverage.xml').exists()
    assert (project_dir / 'htmlcov/index.html').exists()


def test_subpackage(baked_with_development_dependencies):
    project_dir, env_bin = baked_with_development_dependencies
    subpackage = (project_dir / 'my_python_package' / 'mysub')
    subpackage.mkdir()
    (subpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    subsubpackage = (project_dir / 'my_python_package' / 'mysub' / 'mysub2')
    subsubpackage.mkdir()
    (subsubpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    build_output = run([f'python3', 'setup.py', 'build'], project_dir, env_bin)
    assert build_output.returncode == 0
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / '__init__.py').exists()
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / 'mysub2' / '__init__.py').exists()


def test_generate_api_docs(baked_with_development_dependencies):
    project_dir, env_bin = baked_with_development_dependencies

    docs_dir = project_dir / 'docs'
    build_output = run([f'make', 'html'], docs_dir, env_bin)
    assert build_output.returncode == 0
    assert (docs_dir / '_build' / 'html' / 'index.html').exists()
