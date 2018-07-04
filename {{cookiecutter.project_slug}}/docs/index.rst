.. {{ cookiecutter.project_name }} documentation master file, created by
   sphinx-quickstart on Thu Jun 21 11:07:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.project_name }}'s documentation!
==========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

{% if cookiecutter.apidoc == 'yes' %}
API Reference
=============

.. toctree::
  :maxdepth: 2

  {{ cookiecutter.project_slug }} <apidocs/{{ cookiecutter.project_slug }}.rst>
{% endif %}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
