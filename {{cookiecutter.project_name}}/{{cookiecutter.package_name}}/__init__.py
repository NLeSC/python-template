{% if cookiecutter.apidoc == "yes" %}"""Documentation about {{ cookiecutter.package_name }}"""{% endif %}
import logging
from .__version__ import __version__


logging.getLogger(__name__).addHandler(logging.NullHandler())

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
