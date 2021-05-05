"""Tests for the {{ cookiecutter.package_name }}.my_module module.
"""
import pytest

from {{ cookiecutter.package_name }} import my_module


def test_hello():
    assert my_module.hello('nlesc') == 'Hello nlesc!'


def test_hello_with_error():
    with pytest.raises(ValueError) as excinfo:
        my_module.hello('nobody')
        assert str(excinfo.value) == 'Can not say hello to nobody'


@pytest.fixture
def some_name():
    return 'Jane Smith'


def test_hello_with_fixture(some_name):
    assert my_module.hello(some_name) == 'Hello Jane Smith!'
