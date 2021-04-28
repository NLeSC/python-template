# Next steps

## Version control

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
