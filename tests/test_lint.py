""" Lint tests """
import os

import pycodestyle  # formerly known as pep8


def test_pep8_conformance(cookies):
    """Test that we conform to PEP-8."""
    check_paths = [
        'my_python_project',
        'tests',
    ]
    exclude_paths = []

    project = cookies.bake(extra_context={
        'project_short_description': 'short description'})

    print("PEP8 check of directories: {}\n".format(', '.join(check_paths)))

    # Get paths wrt package root
    package_root = str(project.project)
    for paths in (check_paths, exclude_paths):
        for i, path in enumerate(paths):
            paths[i] = os.path.join(package_root, path)

    style = pycodestyle.StyleGuide()
    style.options.exclude.extend(exclude_paths)

    success = style.check_files(check_paths).total_errors == 0

    assert success, "The generated code does not conform to PEP8"
