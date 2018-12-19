# Change Log

## [Unreleased]

### Added

* Fix for displaying wide tables in the documentation (#37)
* Single source version number (+ documentation) (#29)
* Cookiecutter tests (#15)
* Linter test for the generated project
* CITATION.cff
* Support for choosing Python versions (2 and 3) (#20)

### Changed

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
