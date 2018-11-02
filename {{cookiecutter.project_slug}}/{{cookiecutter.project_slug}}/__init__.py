# -*- coding: utf-8 -*-
{% if cookiecutter.apidoc == 'yes' %}"""Documentation about {{ cookiecutter.project_name }}"""{% endif %}

from .__version__ import __version__

__author__ = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
__email__ = '{{ cookiecutter.email }}'
