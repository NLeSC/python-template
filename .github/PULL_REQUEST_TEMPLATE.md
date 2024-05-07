**Description**

- [ ] I have read the [contribution guidelines](https://github.com/NLeSC/python-template/blob/main/CONTRIBUTING.md)
- [ ] This update is in line with what is recommended in the [Python chapter of the Guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python)
- [ ] All user facing changes have been added to CHANGELOG.md

<!-- Description of PR -->

<!--
**Related issues**:
- ...
-->

**Instructions to review the pull request**

<!-- remove what doesn't apply or add more if needed -->
Create a `python-template-test` repo on GitHub (will be overwritten if existing)
```
cd $(mktemp -d --tmpdir py-tmpl-XXXXXX)
cookiecutter -c <pr-branch> https://github.com/<pr-user>/python-template
# Fill with python-template-test info
cd python-template-test
git init
git add --all
git commit -m "First commit"
git remote add origin https://github.com/<you>/python-template-test
git push -u origin main -f
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip setuptools
python -m pip install '.[dev,publishing]'
```
