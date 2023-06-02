"""
WSGI config for playstation_experiment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import configurations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playstation_experiment.settings")
configurations.setup()

application = get_wsgi_application()
