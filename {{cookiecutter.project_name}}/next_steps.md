# Next steps

## Put the generated files under version control

Once your Python package is created, put it under [version
control](https://guide.esciencecenter.nl/#/best_practices/version_control)! We recommend using
[git](http://git-scm.com/) and [github](https://github.com/).

```shell
cd {{ cookiecutter.project_name }}
git init
git add --all
git commit -m "first commit"
git branch -M main
git remote add origin {{ cookiecutter.repository }}
```

Go to
[https://github.com/{{cookiecutter.github_organization}}?tab=repositories](https://github.com/{{cookiecutter.github_organization}}?tab=repositories)
and create a new repository named {{ cookiecutter.project_name }} as an empty repository, then:

```shell
git push --set-upstream origin main
```

## Check automatically generated issues

The generated project comes with a GitHub action
([`.github/workflows/create-issues.yml`](.github/workflows/create-issues.yml)) that adds a couple of issues to the issue
tracker on GitHub ([here]({{cookiecutter.repository}}/issues)). Resolve the issues to complete the setup of your
repository.

## Project layout explained

For an explanation of what files are there, and what each of these do, please refer to [project_setup.md](project_setup.md).
