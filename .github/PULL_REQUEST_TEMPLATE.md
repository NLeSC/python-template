**Description**

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
