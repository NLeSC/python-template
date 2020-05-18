# Change Log

## Unreleased

### Added

* Python 3.5 support in the generated project
* Run template tests for Python 3.7 on appveyor
* Badge table (#52 and #57)

### Changed

* Use pip setup on appveyor (instead of conda)

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
