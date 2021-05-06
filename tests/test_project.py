import os
import subprocess
from pathlib import Path
from shutil import which
from sys import platform
from typing import Sequence

import pytest

IS_WINDOWS = platform.startswith('win')
IS_WINDOWS_CI = IS_WINDOWS and os.environ.get('CI', False)


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
                                       encoding='utf-8')
    print(completed_process.stdout)
    print(completed_process.stderr)
    return completed_process


@pytest.fixture
def project_env_bin_dir(tmp_path):
    if IS_WINDOWS_CI:
        # Creating virtualenv does not work on Windows CI,
        # falling back to using current pip3 dir
        pip = Path(which('pip3'))
        bin_dir = pip.parent
    else:
        env_output = run(['python3', '-m', 'venv', 'env'], tmp_path)
        assert env_output.returncode == 0
        bin_dir = str(tmp_path / 'env' / 'bin')
        if IS_WINDOWS:
            bin_dir = str(tmp_path / 'env' / 'Scripts')
    return str(bin_dir) + os.sep


@pytest.fixture
def baked_with_development_dependencies(cookies, project_env_bin_dir):
    result = cookies.bake()
    assert result.exit_code == 0
    bin_dir = project_env_bin_dir
    latest_pip_output = run([f'{bin_dir}pip3', 'install', '--upgrade', 'pip', 'setuptools'], result.project)
    assert latest_pip_output.returncode == 0
    pip_output = run([f'{bin_dir}pip3', 'install', '--editable', '.[dev]'], result.project)
    assert pip_output.returncode == 0
    return result.project


def test_pytest(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir
    result = run([f'{bin_dir}pytest'], project_dir)
    assert result.returncode == 0
    assert '== 3 passed in' in result.stdout
    assert (project_dir / 'coverage.xml').exists()
    assert (project_dir / 'htmlcov' / 'index.html').exists()


def test_subpackage(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir
    subpackage = (project_dir / 'my_python_package' / 'mysub')
    subpackage.mkdir()
    (subpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    subsubpackage = (project_dir / 'my_python_package' / 'mysub' / 'mysub2')
    subsubpackage.mkdir()
    (subsubpackage / '__init__.py').write_text('FOO = "bar"', encoding="utf-8")

    if IS_WINDOWS_CI:
        # On Windows CI python and pip executable are in different paths
        bin_dir = ''
    result = run([f'{bin_dir}python', 'setup.py', 'build'], project_dir)
    assert result.returncode == 0
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / '__init__.py').exists()
    assert (project_dir / 'build' / 'lib' / 'my_python_package' / 'mysub' / 'mysub2' / '__init__.py').exists()


def test_generate_api_docs(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir

    result = run([f'{bin_dir}sphinx-build', '-b', 'html', 'docs', 'docs/_build/html'], project_dir)
    assert result.returncode == 0
    assert 'build succeeded' in result.stdout
    assert (project_dir / 'docs' / '_build' / 'html' / 'index.html').exists()


def test_coverage_api_docs(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir

    result = run([f'{bin_dir}sphinx-build', '-b', 'coverage', 'docs', 'docs/_build/coverage'], project_dir)
    assert result.returncode == 0
    assert 'build succeeded' in result.stdout
    coverage_file = project_dir / 'docs' / '_build' / 'coverage' / 'python.txt'
    lines = coverage_file.readlines()
    assert len(lines) == 2


def test_doctest_api_docs(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir

    result = run([f'{bin_dir}sphinx-build', '-b', 'doctest', 'docs', 'docs/_build/doctest'], project_dir)
    assert result.returncode == 0
    assert 'build succeeded' in result.stdout
    assert (project_dir / 'docs' / '_build' / 'doctest' / 'output.txt').exists()


def test_prospector(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir

    result = run([f'{bin_dir}prospector'], project_dir)
    assert result.returncode == 0
    assert 'Messages Found: 0' in result.stdout


def test_isort_check(baked_with_development_dependencies, project_env_bin_dir):
    project_dir, bin_dir = baked_with_development_dependencies

    result = run([f'{bin_dir}isort', '--recursive', '--check-only', 'my_python_package'], project_dir)
    assert result.returncode == 0
    assert '' in result.stdout


def test_bumpversion(baked_with_development_dependencies, project_env_bin_dir):
    project_dir = baked_with_development_dependencies
    bin_dir = project_env_bin_dir

    original_version = '0.1.0'
    assert original_version in (project_dir / 'setup.cfg').read_text('utf-8')
    assert original_version in (project_dir / 'CITATION.cff').read_text('utf-8')
    assert original_version in (project_dir / 'my_python_package' / '__init__.py').read_text('utf-8')
    assert original_version in (project_dir / 'docs' / 'conf.py').read_text('utf-8')

    result = run([f'{bin_dir}bumpversion', 'major'], project_dir)
    assert result.returncode == 0
    assert '' in result.stdout
    expected_version = '1.0.0'
    assert expected_version in (project_dir / 'setup.cfg').read_text('utf-8')
    assert expected_version in (project_dir / 'CITATION.cff').read_text('utf-8')
    assert expected_version in (project_dir / 'my_python_package' / '__init__.py').read_text('utf-8')
    assert expected_version in (project_dir / 'docs' / 'conf.py').read_text('utf-8')
