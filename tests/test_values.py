import pytest


def test_double_quotes_in_name_and_description(cookies):
    ctx = {
        "project_short_description": '"double quotes"',
        "full_name": '"name"name'
    }
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0


def test_single_quotes_in_name_and_description(cookies):
    ctx = {
        "project_short_description": "'single quotes'",
        "full_name": "Mr. O'Keeffe"
    }
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0


def test_dash_in_project_slug(cookies):
    ctx = {
        "project_slug": "my-package"
    }
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0


def test_space_in_project_slug(cookies):
    ctx = {
        "project_slug": "my package"
    }
    project = cookies.bake(extra_context=ctx)

    assert project.exit_code == 0
