"""
WSGI config for radiopolka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

import conf

path = conf.PROJECT_PATH
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "radiopolka.settings")

application = get_wsgi_application()
