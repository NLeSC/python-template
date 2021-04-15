import sys

# Note: cookiecutter first makes the main level directory using
# project_name from cookiecutter.json before running this hook

{{ cookiecutter.update({
    "package_name": cookiecutter.package_name.lower().replace(" ", "_").replace("-", "_"),
    "project_name": cookiecutter.project_name.lower().replace(" ", "-"),
    "full_name": cookiecutter.full_name.replace('\"', '\\\"'),
    "repository": "https://github.com/" + cookiecutter.github_organization + "/" + cookiecutter.project_name.lower().replace("-", "_"),
    "package_short_description": cookiecutter.package_short_description.replace('\"', '\\\"')
}) }}

sys.exit(0)
