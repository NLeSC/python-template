# Change Log

## Unreleased

### Added

* Python 3.5 support in the generated project
* Run template tests for Python 3.7 on appveyor
* Badge table (#52 and #57)
* Remove requirements.txt (discussion: https://github.com/NLeSC/guide/issues/156) #67
* Issue templates #159
* Cffconvert github action #91
* Mlc gh action
* Developer documentation for generated package and template itself
* Post hook to point to document with more information
* Migrated to static setup.cfg as per the recommended practice #84
* Pre-commit git hook to automatically run the linters before committing to github #82
* Sonarcloud integration for static analysis and code coverage #172
* CoC for generated package
* Generated package with badges

### Changed

* Use pip setup on appveyor (instead of conda)
* Replaced requirements deps to setup.cfg|py #67
* Replaced rst format by markdown #190 #162
* Replaced appveyor with gha matrix build for generated project, support all current python versions and windows, linux, mac #160
* Updated CITATION.cff, .zenodo.json; removed codemeta.json #127 #137
* Updated CoC
* Simplified templating variables using pre project hook #82
* Consolidated pytest.ini into setup.cfg #155
* Versioning now handled with bump2version #192
* Updated project_setup.md #165

## Removed

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
