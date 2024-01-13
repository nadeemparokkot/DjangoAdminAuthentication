"""
ASGI config for sample_11_serversidelogin_inbuild project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_11_serversidelogin_inbuild.settings')

application = get_asgi_application()
