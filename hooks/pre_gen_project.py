# Note: cookiecutter first makes the main level directory using
# directory_name from cookiecutter.json before running this hook

{{ cookiecutter.update({
    "package_name": cookiecutter.package_name.lower().replace(" ", "_").replace("-", "_"),
    "directory_name": cookiecutter.directory_name.lower().replace(" ", "-"),
    "full_name": cookiecutter.full_name.replace('\"', '\\\"'),
    "repository": "https://github.com/" + cookiecutter.github_organization + "/" + cookiecutter.directory_name.lower().replace(" ", "-"),
    "package_short_description": cookiecutter.package_short_description.replace('\"', '\\\"')
}) }}
