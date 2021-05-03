import os
import subprocess
from pathlib import Path
from sys import platform, executable
from typing import Sequence

import pytest


def test_project_folder(cookies):
    project = cookies.bake()

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename == 'my-python-project'
    assert project.project.isdir()


def run(args: Sequence[str], dirpath: os.PathLike) -> subprocess.CompletedProcess:
    completed_process = subprocess.run(args=args,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       cwd=dirpath,
                                       encoding="utf-8")
    print(completed_process.stdout)
    print(completed_process.stderr)
    return completed_process


@pytest.fixture
def baked_with_development_dependencies(cookies):
    result = cookies.bake()
    if platform.startswith("win") and os.environ.get('CI', False):
        # Creating virtualenv does not work on Windows CI,
        # falling back to using current Python
        bin_dir = str(Path(executable).parent) + '\\'
        print(bin_dir)
        print(list(bin_dir.iterdir()))
    else:
        env_output = run(['python3', '-m', 'venv', 'env'], result.project)
        assert env_output.returncode == 0
        bin_dir = 'env/Scripts/' if platform.startswith("win") else 'env/bin/'
    latest_pip_output = run([f'{bin_dir}pip', 'install', '--upgrade', 'pip', 'setuptools'], result.project)
    assert latest_pip_output.returncode == 0
    pip_output = run([f'{bin_dir}pip', 'install', '--editable', '.[dev]'], result.project)
    assert pip_output.returncode == 0
    return result.project, bin_dir


def test_pytest(baked_with_development_dependencies):
    project_dir, bin_dir = baked_with_development_dependencies
    pytest_output = run([f'{bin_dir}pytest'], project_dir)
    assert pytest_output.returncode == 0
    assert '== 3 passed in' in pytest_output.stdout
    assert (project_dir / 'coverage.xml').exists()
    assert (project_dir / 'htmlcov/index.html').exists()


def test_subpackage(baked_with_development_dependencies):
    project_dir, bin_dir = baked_with_development_dependencies
    subpackage = (project_dir / 'my_python_package' / 'mysub')
    subpackage.mkdir()
    (subpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    subsubpackage = (project_dir / 'my_python_package' / 'mysub' / 'mysub2')
    subsubpackage.mkdir()
    (subsubpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    build_output = run([f'{bin_dir}python', 'setup.py', 'build'], project_dir)
    assert build_output.returncode == 0
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / '__init__.py').exists()
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / 'mysub2' / '__init__.py').exists()


def test_generate_api_docs(baked_with_development_dependencies):
    project_dir, bin_dir = baked_with_development_dependencies

    build_output = run([f'{bin_dir}sphinx-build', '-b', 'html', 'docs', 'docs/_build/html'], project_dir)
    assert build_output.returncode == 0
    assert 'build succeeded' in build_output.stdout
    assert (project_dir / 'docs' / '_build' / 'html' / 'index.html').exists()
