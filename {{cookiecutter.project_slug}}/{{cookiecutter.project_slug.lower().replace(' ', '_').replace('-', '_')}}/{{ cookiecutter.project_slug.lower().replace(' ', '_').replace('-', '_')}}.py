# -*- coding: utf-8 -*-
{%-if cookiecutter.apidoc == 'yes' %}"""Documentation about the {{ cookiecutter.project_name }} module."""{% endif %}
import logging

logger = logging.getLogger(__name__)


# FIXME: put actual code here
def example():
    logger.info('Providing information about the excecution of the function.')
