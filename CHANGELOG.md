# Change Log

## [Unreleased]

### Added

### Changed

### Removed

## 0.6.1

### Added

* Add .gitignore and .editorconfig to the list of files that are not updated if they exist [#655](https://github.com/NLeSC/python-template/pull/655)

### Changed

* copyright owner is asked in all profiles [#629](https://github.com/NLeSC/python-template/pull/629)
* license files includes year and copyright owner information [#629](https://github.com/NLeSC/python-template/pull/629)
* combine all the next step jobs in a single workflow [#657](https://github.com/NLeSC/python-template/pull/657)
* fix CITATION.cff validation issues which also helps cffconvert workflow to pass [#657](https://github.com/NLeSC/python-template/pull/657)

### Removed

* Remove pyproject.toml and CITATION.cff from the list of files that are not updated if they exist [#655](https://github.com/NLeSC/python-template/pull/655)

## [0.6.0]

### Added

* Keep project_setup.md for all the profiles and remove from the menu [#576](https://github.com/NLeSC/python-template/pull/576)
* Make contributing guidelines optional [#465](https://github.com/NLeSC/python-template/pull/465)
* Make linting optional [#568](https://github.com/NLeSC/python-template/pull/568)
* Make editorconfig optional [#571](https://github.com/NLeSC/python-template/pull/571)
* Make contributing guidelines optional [#465](https://github.com/NLeSC/python-template/pull/465)
* Make developer documentation optional [#467](https://github.com/NLeSC/python-template/pull/541)
* Make Code of Conduct optional [#464](https://github.com/NLeSC/python-template/pull/530)
* New YAML files for copier questions [#529](https://github.com/NLeSC/python-template/pull/529)
* Make zenodo next step instructions optional [#520](https://github.com/NLeSC/python-template/pull/520)
* Make SonarCloud optional [#515](https://github.com/NLeSC/python-template/pull/515)
* Make citation optional [#471](https://github.com/NLeSC/python-template/pull/471)
* Make online documentation optional [#476](https://github.com/NLeSC/python-template/pull/476)
* Make local documentation optional [#593](https://github.com/NLeSC/python-template/pull/593)
* Make local test optional [#594](https://github.com/NLeSC/python-template/pull/594)

### Changed

* Update the user documentation (README.md) of the template [#575](https://github.com/NLeSC/python-template/pull/623)
* Updated .gitignore [#622](https://github.com/NLeSC/python-template/pull/622)
* add extra info for sub-menus [#628](https://github.com/NLeSC/python-template/pull/628)
* skip merging CHANGELOG.md and CODE_OF_CONDUCT.md if they exist [#628](https://github.com/NLeSC/python-template/pull/628)
* added value field to license options [#617](https://github.com/NLeSC/python-template/pull/617)
* fix filename typo of githooks [#611](https://github.com/NLeSC/python-template/pull/609)
* next_steps.md is shown as a copier message [#609](https://github.com/NLeSC/python-template/pull/609)
* Change the default profile to 'recommended' [#598](https://github.com/NLeSC/python-template/pull/598)
* Updated the user documentation (README.md) of the template [#569](https://github.com/NLeSC/python-template/pull/569)
* Droped Python 3.8 and 3.9 support [#551](https://github.com/NLeSC/python-template/pull/551)
* Fix broken link checker [#546](https://github.com/NLeSC/python-template/pull/546)
* pre-commit script is optional ([#457](https://github.com/NLeSC/python-template/issues/457))
* CHANGELOG.md is now optional ([#462](https://github.com/NLeSC/python-template/issues/462))
* Restored default line-length of 79 characters, as recommended by [PEP-8](https://peps.python.org/pep-0008/#maximum-line-length) [#389](https://github.com/NLeSC/python-template/pull/389)

### Removed

* Remove the configuration of isort ([#591](https://github.com/NLeSC/python-template/pull/591)), which is no longer used since [#347](https://github.com/NLeSC/python-template/issues/347).

## [0.5.0]

Released on August 15, 2024

### Added

* Added Python 3.12 support [#356](https://github.com/NLeSC/python-template/issues/356)
* Template unit tests for documentation generation, linting and version bumping
* Docstring for function
* Intersphinx to documentation
* Coverage and doctest commands for documentation [#97](https://github.com/NLeSC/python-template/issues/97)
* Added new 'docs' section in extra dependencies [#317](https://github.com/NLeSC/python-template/issues/317)

### Changed

* Made copier configuration more modular [#529](https://github.com/NLeSC/python-template/pull/529)
* pre-commit script is optional ([#457](https://github.com/NLeSC/python-template/issues/457))
* CHANGELOG.md is now optional ([#462](https://github.com/NLeSC/python-template/issues/462))
* Moved to src/ based layout for generated packages
* Moved from setup.cfg/.py to pyproject.toml [#351](https://github.com/NLeSC/python-template/issues/351)
* Moved from prospector to ruff [#336](https://github.com/NLeSC/python-template/issues/336)
* Renamed `project_name` to `directory_name` in cookiecutter questionnaire
* Initial linting is error free [#227](https://github.com/NLeSC/python-template/issues/227)
* Consolidated test/lint/build/docs into single matrix workflow [#270](https://github.com/NLeSC/python-template/issues/276)
* Enforce isort configuration
* Default for `package_short_description` in cookiecutter questionnaire
* Link checker ignores GH private pages and test pypi site [#288](https://github.com/NLeSC/python-template/issues/288)
* In CI build workflow make prospector die if there are errors [#275](https://github.com/NLeSC/python-template/issues/275)
* All example tests make use of example function
* Use bumpversion for version in Sphinx config [#44](https://github.com/NLeSC/python-template/issues/44)
* Regenerated docs/conf.py with sphinx-quickstart v3.5.4 + enabled built-in extensions [#44](https://github.com/NLeSC/python-template/issues/44)
* Generate api rst files with extension instead of custom function [#95](https://github.com/NLeSC/python-template/issues/95)
* Change from bump2version (unmaintained) to bump-my-version.
* Set markdown link checker to quiet mode: only report broken links [#262](https://github.com/NLeSC/python-template/issues/262)

### Removed

* Removed Python 3.7 support [#343](https://github.com/NLeSC/python-template/issues/343)
* `.pylintrc` file, was too strict, too soon [#267](https://github.com/NLeSC/python-template/issues/267)
* Unused development dependencies [#167](https://github.com/NLeSC/python-template/issues/167)
* Statements in project_setup.md already mentioned in README.dev.md
* .zenodo.json is no longer necessary, CITATION.cff also works with Zenodo.

## [0.4.0]

Released on May 3, 2021

### Added

* Instructions to add your existing code to directory generated by the NLeSC Python template [#202](https://github.com/NLeSC/python-template/issues/202)
* Keywords to questionnaire [#270](https://github.com/NLeSC/python-template/issues/270)
* Next step issue generation workflow [#228](https://github.com/NLeSC/python-template/issues/228)
* Next step issue for SonarCloud integration [#234](https://github.com/NLeSC/python-template/issues/234)
* Next step issue for Zenodo integration [#235](https://github.com/NLeSC/python-template/issues/235)
* Next step issue for Read the Docs [#236](https://github.com/NLeSC/python-template/issues/236)
* Next step issue for citation data [#237](https://github.com/NLeSC/python-template/issues/237)
* Next step issue for linting [#238](https://github.com/NLeSC/python-template/issues/238)
* Next steps documentation [#240](https://github.com/NLeSC/python-template/issues/240)
* Support for sub packages in distro [#160](https://github.com/NLeSC/python-template/issues/160)
* Tests for api doc generation [#213](https://github.com/NLeSC/python-template/issues/213)
* CI Tests on Windows [#140](https://github.com/NLeSC/python-template/issues/140) [#223](https://github.com/NLeSC/python-template/issues/223)
* `.pylintrc` file
* Valid license name and first author name in `CITATION.cff`
* SonarCloud integration for code quality and coverage [#89](https://github.com/NLeSC/python-template/issues/89)
* Read the Docs [#78](https://github.com/NLeSC/python-template/issues/78)

### Changed

* Always generate API docs [#176](https://github.com/NLeSC/python-template/issues/176)
* Have 100% test coverage in generated code [#88](https://github.com/NLeSC/python-template/issues/88)

### Removed

* Automatic publish to PyPi after GitHub release [#196](https://github.com/NLeSC/python-template/issues/196)

## [0.3.0]

Released on Apr 22, 2021

### Added

* Added Python 3.9 support
* Template is being tested for Python 3.6, 3.7, 3.8, 3.9
* Added extra badges such as fair-software.eu badges and SonarCloud, GitHub Actions [#52](https://github.com/NLeSC/python-template/issues/52) [#57](https://github.com/NLeSC/python-template/issues/57)
* Added issue templates [#159](https://github.com/NLeSC/python-template/issues/159)
* Added cffconvert GitHub action [#91](https://github.com/NLeSC/python-template/issues/91)
* Added Markdown Link Checker GitHub action
* Added Developer documentation
* Added cookiecutter post-hook to point to document with more information
* Migrated to static setup.cfg as per the recommended practice [#84](https://github.com/NLeSC/python-template/issues/84)
* Added Pre-commit githook to automatically run the linters before committing to GitHub [#82](https://github.com/NLeSC/python-template/issues/82)
* Added Sonarcloud integration for static analysis and code coverage [#172](https://github.com/NLeSC/python-template/issues/172)
* Added badges to the generated package

### Changed

* Moved requirements.txt dependencies to setup.cfg and removed requirements.txt [#67](https://github.com/NLeSC/python-template/issues/67)
* Replaced all ReStructuredText (rst) files by Markdown [#190](https://github.com/NLeSC/python-template/issues/190) [#162](https://github.com/NLeSC/python-template/issues/162)
* Use matrix build for generated project to support all current Python versions on Windows, Linux, Mac [#160](https://github.com/NLeSC/python-template/issues/160)
* Updated CITATION.cff, .zenodo.json; removed codemeta.json [#127](https://github.com/NLeSC/python-template/issues/127) [#137](https://github.com/NLeSC/python-template/issues/137)
* Updated Code of Conduct of the template
* Simplified templating variables using cookiecutter pre-hook [#82](https://github.com/NLeSC/python-template/issues/82)
* Consolidated pytest.ini into setup.cfg [#155](https://github.com/NLeSC/python-template/issues/155)
* Versioning now handled with bump2version [#192](https://github.com/NLeSC/python-template/issues/192)
* Updated project_setup.md [#165](https://github.com/NLeSC/python-template/issues/165)
* Updated Code of Conduct for generated package
* Improved the documentation for the generated package and template itself

### Removed

* Dropped appveyor [#160](https://github.com/NLeSC/python-template/issues/160)
* Dropped everything Conda related
* Drop Python 3.5 support
* Removed unit tests doing the linting

## [0.2.0]

Released on July 17, 2019

### Added

* Set up logging and provide a logging example (#9)
* Fix for displaying wide tables in the documentation (#37)
* Single source version number (+ documentation) (#29)
* Cookiecutter tests (#15)
* Linter test for the generated project
* CITATION.cff
* Support for pypi deployment using travis (#36)

### Changed

* Replace dashes and spaces in project_slug with underscore (#33)
* Put project setup documentation in a separate document (#39)
* Fix numbered lists in .rst files (#40)
* Added rst, y(a)ml and cwl to .editorconfig (#35)
* Default documentation theme is `sphinx_rtd_theme` (#34)
* Improve licensing
* Fix example tests that failed to run (#28)
* Remove quotes from project name and project description (#27)
* Update prospector configuration (#26)
 	* Make prospector less strict
 	* Have prospector ignore the docs directory
* Add `install_requires` to `setup.py` (#21)
* Improved .gitignore (#22)
* More detailed documentation about
 	* Project setup
 	* Setup instructions
 	* NOTICE file

### Removed

* Python 2 support

## [0.1.0]

Released on July 12, 2018.

### Added

* First version of the Python project template that follows the Netherlands eScience Center software development guide, containing:
 	* Tests,
 	* Documentation,
 	* Code style checking
 	* Editorconfig
 	* Default Travis configuration
 	* Change log
 	* Code of Conduct
 	* Contributing guidelines
 	* License
 	* Manifest.in
 	* README
 	* Requirements.txt
 	* Setup configuration

[Unreleased]: https://github.com/NLeSC/python-template//compare/0.5.0...HEAD
[0.5.0]:      https://github.com/NLeSC/python-template/releases/tag/0.5.0
[0.4.0]:      https://github.com/NLeSC/python-template/releases/tag/0.4.0
[0.3.0]:      https://github.com/NLeSC/python-template/releases/tag/0.3.0
[0.2.0]:      https://github.com/NLeSC/python-template/releases/tag/0.2.0
[0.1.0]:      https://github.com/NLeSC/python-template/releases/tag/0.1.0
