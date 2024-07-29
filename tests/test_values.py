def test_double_quotes_in_name_and_description(copie):
    ctx = {
        "project_short_description": '"double quotes"',
        "full_name": '"name"name'
    }
    project = copie.copy(extra_answers=ctx)

    assert project.exit_code == 0


def test_single_quotes_in_name_and_description(copie):
    ctx = {
        "project_short_description": "'single quotes'",
        "full_name": "Mr. O'Keefe"
    }
    project = copie.copy(extra_answers=ctx)

    assert project.exit_code == 0


def test_dash_in_directory_name(copie):
    ctx = {
        "directory_name": "my-python-project"
    }
    project = copie.copy(extra_answers=ctx)

    assert project.exit_code == 0


def test_space_in_directory_name(copie):
    ctx = {
        "directory_name": "my python project"
    }
    project = copie.copy(extra_answers=ctx)

    assert project.exit_code == 0
