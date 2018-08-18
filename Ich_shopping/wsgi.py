"""
WSGI config for Ich_shopping project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi
path='/home/centos/public_html/Ich_shopping'
if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ich_shopping.settings")

application = get_wsgi_application()
