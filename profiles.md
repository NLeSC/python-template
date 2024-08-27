# Template Profiles
- package_name:
- version:
- template_profile:
  - minumum --> DONE
  - recommeded --> all questions - excluded with the defaults
  - optional --> all questions with answers off

- github_organization:
- full_name:
- email:
- copyright_holder:
- licence (exist)

- community:
  - code of conduct --> if TRUE ask for email
  - contributing guidelines

- documentation
  - developer documentation
  - online documentation (read the docs)
  - project_setup.md

- code quality:
  - sonarcloud #515
  - ruff and lint workflow
  - github action to build (exist) #451
  - pre-commit
  - .editorconfig

- publishing and release
  - zenodo #520 
  - keywords
  - changelog.md
  - cffconvert workflow and citation file

- markdown link checker workflow

## Minimum

- src/
- docs/
- test/
- pyproject.toml
- README.md
- .gitignore
- MANIFEST.in
- LICENCE

## Questions to exclude from recommended
- Link checker
- pre-commit
- changelog.md
- project_setup.md
