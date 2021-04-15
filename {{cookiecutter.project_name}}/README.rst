.. list-table::
   :widths: 25 25
   :header-rows: 1

   * - fair-software.nl recommendations
     - Badges
   * - \1. Code repository
     - |GitHub Badge|
   * - \2. License
     - |License Badge|
   * - \3. Community Registry
     - |PyPI Badge| |Research Software Directory Badge|
   * - \4. Enable Citation
     - |Zenodo Badge|
   * - \5. Checklist
     - |CII Best Practices Badge|
   * - **Other best practices**
     -
   * - Continuous integration
     - |Python Build| |PyPI Publish|
   * - Metadata consistency
     - |metadata consistency|

(Customize these badges with your own links, and check https://shields.io/ or https://badgen.net/ to see which other badges are available.)

.. |GitHub Badge| image:: https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue
   :target: {{ cookiecutter.repository }}
   :alt: GitHub Badge

.. |License Badge| image:: https://img.shields.io/github/license/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_name }}
   :target: {{ cookiecutter.repository }}
   :alt: License Badge

.. |PyPI Badge| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg?colorB=blue
   :target: https://pypi.python.org/project/{{ cookiecutter.project_name }}/
   :alt: PyPI Badge

.. |Research Software Directory Badge| image:: https://img.shields.io/badge/rsd-{{ cookiecutter.project_name }}-00a3e3.svg
   :target: https://www.research-software.nl/software/{{ cookiecutter.project_name }}
   :alt: Research Software Directory Badge

..
    Goto https://zenodo.org/account/settings/github/ to enable Zenodo/GitHub integration.
    After creation of a GitHub release at {{ cookiecutter.repository }}/releases
    there will be a Zenodo upload created at https://zenodo.org/deposit with a DOI, this DOI can be put in the Zenodo badge urls.
    In the README, we prefer to use the concept DOI over versioned DOI, see https://help.zenodo.org/#versioning.
.. |Zenodo Badge| image:: https://zenodo.org/badge/DOI/< replace with created DOI >.svg
   :target: https://doi.org/<replace with created DOI>
   :alt: Zenodo Badge

..
    A CII Best Practices project can be created at https://bestpractices.coreinfrastructure.org/en/projects/new
.. |CII Best Practices Badge| image:: https://bestpractices.coreinfrastructure.org/projects/< replace with created project identifier >/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/< replace with created project identifier >
   :alt: CII Best Practices Badge

.. |Python Build| image:: {{ cookiecutter.repository }}/workflows/Python/badge.svg
   :target: {{ cookiecutter.repository }}/actions?query=workflow%3A%22Python%22
   :alt: Python Build

.. |PyPI Publish| image:: {{ cookiecutter.repository }}/workflows/PyPI/badge.svg
   :target: {{ cookiecutter.repository }}/actions?query=workflow%3A%22PyPI%22
   :alt: PyPI Publish

.. |metadata consistency| image:: {{ cookiecutter.repository }}/workflows/cffconvert/badge.svg
   :target: {{ cookiecutter.repository }}/actions?query=workflow%3A%22cffconvert%22
   :alt: metadata consistency badge

################################################################################
{{ cookiecutter.project_name }}
################################################################################

{{ cookiecutter.package_short_description }}


The project setup is documented in `a separate document <project_setup.rst>`_. Feel free to remove this document (and/or the link to this document) if you don't need it.

Installation
------------

To install {{ cookiecutter.project_name }}, do:

.. code-block:: console

  git clone {{ cookiecutter.repository }}.git
  cd {{ cookiecutter.project_name }}
  python3 -m pip install .


Run tests (including coverage) with:

.. code-block:: console

  python3 setup.py test


Documentation
*************

.. _README:

Include a link to your project's full documentation here.

Contributing
************

If you want to contribute to the development of {{ cookiecutter.project_name }},
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

Credits
*******

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
