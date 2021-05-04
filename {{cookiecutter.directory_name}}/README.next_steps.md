# Next steps

## Put the generated files under version control

Once your Python package is created, put it under [version
control](https://guide.esciencecenter.nl/#/best_practices/version_control) using
[git](https://git-scm.com/) and [GitHub](https://github.com/).

```shell
cd {{ cookiecutter.directory_name }}
git init
git add --all
git commit -m "first commit"
git branch -M main
git remote add origin {{ cookiecutter.repository }}
```

## Push the initial commit to a new repo on GitHub

Go to
[https://github.com/organizations/{{cookiecutter.github_organization}}/repositories/new](https://github.com/organizations/{{cookiecutter.github_organization}}/repositories/new)
and create a new repository named `{{ cookiecutter.directory_name }}` as an empty repository, then push your commits to GitHub:

```shell
git push --set-upstream origin main
```

## Check automatically generated issues

A short while after you push your commits to GitHub for the first time, a few issues outlining next steps will added
automatically ([here]({{cookiecutter.repository}}/issues?q=author%3Aapp%2Fgithub-actions)). Resolve them to complete the
setup of your repository.

## Project layout explained

For an explanation of what files are there, and what each of these do, please refer to [README.project_layout_explained.md](README.project_layout_explained.md).
