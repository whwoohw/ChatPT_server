"""
WSGI config for chatpt_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import subprocess
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatpt_server.settings')
cmd_1 = "brew install tesseract"
cmd_2 = "which tesseract"
p1 = subprocess.call(cmd_1, shell=True)
p2 = subprocess.call(cmd_2, shell=True)
application = get_wsgi_application()
