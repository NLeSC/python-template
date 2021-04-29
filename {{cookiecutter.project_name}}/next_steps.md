# Next steps

## Put the generated files under version control

Once your Python package is created, put it under [version
control](https://guide.esciencecenter.nl/#/best_practices/version_control) using
[git](http://git-scm.com/) and [GitHub](https://github.com/).

```shell
cd {{ cookiecutter.project_name }}
git init
git add --all
git commit -m "first commit"
git branch -M main
git remote add origin {{ cookiecutter.repository }}
```

## Push the initial commit to a new repo on GitHub

Go to
[https://github.com/{{cookiecutter.github_organization}}/repositories/new](https://github.com/{{cookiecutter.github_organization}}/repositories/new)
and create a new repository named `{{ cookiecutter.project_name }}` as an empty repository, then push your commits to GitHub:

```shell
git push --set-upstream origin main
```

## Check automatically generated issues

The first time you push to GitHub, a few issues outlining next steps will be added automatically
([here]({{cookiecutter.repository}}/issues?q=author%3Aapp%2Fgithub-actions)). Resolve them to complete the setup of your
repository.

## Project layout explained

For an explanation of what files are there, and what each of these do, please refer to [project_setup.md](project_setup.md).
