# Change Log

## Unreleased


## 0.3.0

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

* Added requirements.txt dependencies to setup.cfg and removed requirements.txt [#67](https://github.com/NLeSC/python-template/issues/67)
* Replaced rst format by markdown [#190](https://github.com/NLeSC/python-template/issues/190) [#162](https://github.com/NLeSC/python-template/issues/162)
* Replaced appveyor with gha matrix build for generated project, support all current python versions and Windows, Linux, Mac [#160](https://github.com/NLeSC/python-template/issues/160)
* Updated CITATION.cff, .zenodo.json; removed codemeta.json [#127](https://github.com/NLeSC/python-template/issues/127) [#137](https://github.com/NLeSC/python-template/issues/137)
* Updated CoC
* Simplified templating variables using pre project hook [#82](https://github.com/NLeSC/python-template/issues/82)
* Consolidated pytest.ini into setup.cfg [#155](https://github.com/NLeSC/python-template/issues/155)
* Versioning now handled with bump2version [#192](https://github.com/NLeSC/python-template/issues/192)
* Updated project_setup.md [#165](https://github.com/NLeSC/python-template/issues/165)
* Updated Code of Conduct for generated package
* Improved the documentation for the generated package and template itself

## Removed
* Drop appveyor
* Evrything Conda related
* Python 3.5 support
* Unit test that was acting as a linter, replaced with actual linter documented in README.dev.md


## 0.2.0

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
	- Make prospector less strict
	- Have prospector ignore the docs directory
* Add `install_requires` to `setup.py` (#21)
* Improved .gitignore (#22)
* More detailed documentation about
	- Project setup
	- Setup instructions
	- NOTICE file

### Removed

* Python 2 support

## 0.1.0

Released on July 12, 2018.

### Added

* First version of the Python project template that follows the Netherlands eScience Center software development guide, containing:
	- Tests,
	- Documentation,
	- Code style checking
	- Editorconfig
	- Default Travis configuration
	- Change log
	- Code of Conduct
	- Contributing guidelines
	- License
	- Manifest.in
	- README
	- Requirements.txt
	- Setup configuration
