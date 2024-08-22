from test_project import copier_project_defaults

def test_double_quotes_in_name_and_description(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    test_values = {
        "project_short_description": '"double quotes"',
        "full_name": '"name"name'
    }
    project_defaults.update(test_values)
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0


def test_single_quotes_in_name_and_description(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    test_values = {
        "project_short_description": "'single quotes'",
        "full_name": "Mr. O'Keefe"
    }
    project_defaults.update(test_values)
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0
