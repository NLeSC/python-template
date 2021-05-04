"""Tests for the {{ cookiecutter.package_name }}.my_module module.
"""
import pytest

from {{ cookiecutter.package_name }} import my_module


def test_hello():
    assert my_module.hello('nlesc') == 'Hello nlesc!'


def test_hello_without_arguments():
    with pytest.raises(TypeError):
        my_module.hello()
