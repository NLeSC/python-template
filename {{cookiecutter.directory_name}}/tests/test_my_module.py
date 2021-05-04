"""Tests for the {{ cookiecutter.package_name }}.my_module module.
"""
from {{ cookiecutter.package_name }} import my_module


def test_hello():
    assert my_module.hello('nlesc') == 'Hello nlesc!'
