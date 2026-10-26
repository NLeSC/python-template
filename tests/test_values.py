import tomllib

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


def test_keywords_are_trimmed(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    project_defaults.update({"keywords": "kw1, second kw , kw3"})
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0
    pyproject = tomllib.loads((project.project_dir / "pyproject.toml").read_text())
    assert pyproject["project"]["keywords"] == ["kw1", "second kw", "kw3"]
    citation = (project.project_dir / "CITATION.cff").read_text()
    assert '  - "kw1"\n  - "second kw"\n  - "kw3"\n' in citation


def test_empty_keywords_are_omitted(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    project_defaults.update({"keywords": ""})
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0
    pyproject = tomllib.loads((project.project_dir / "pyproject.toml").read_text())
    assert pyproject["project"]["keywords"] == []
    assert "keywords" not in (project.project_dir / "CITATION.cff").read_text()
