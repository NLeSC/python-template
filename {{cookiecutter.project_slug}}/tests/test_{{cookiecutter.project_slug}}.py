#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the {{ cookiecutter.project_slug }} module.
"""
import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_{{ cookiecutter.project_slug }}(an_object):
    assert an_object == {}
