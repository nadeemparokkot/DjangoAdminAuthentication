"""
WSGI config for sample_11_serversidelogin_inbuild project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_11_serversidelogin_inbuild.settings')

application = get_wsgi_application()
