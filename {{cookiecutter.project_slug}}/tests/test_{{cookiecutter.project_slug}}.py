#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the {{ cookiecutter.project_slug }} module.
"""
import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def_test_without_test_object():
    assert False


class Test{{ cookiecutter.project_slug|title }}(object):
    @pytest.fixture
    def {{ cookiecutter.project_slug }}(self):
        pass

    def test_{{ cookiecutter.project_slug }}(self, {{ cookiecutter.project_slug }}):
        assert False

    def test_with_error(self, {{ cookiecutter.project_slug }}):
        with pytest.raises(ValueError):
            pass
