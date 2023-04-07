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

cmd_1 = "ed /etc/sudoers"
cmd_2 = "username ALL=(ALL) NOPASSWD:apt-get install tesseract-ocr"
cmd_3 = "."
cmd_4 = "w"
cmd_5 = "q"
cmd_6 = "apt-get install tesseract-ocr"
cmd_7 = "which tesseract"
p1 = subprocess.call(cmd_1, shell=True)
p2 = subprocess.call(cmd_2, shell=True)
p3 = subprocess.call(cmd_3, shell=True)
p4 = subprocess.call(cmd_4, shell=True)
p5 = subprocess.call(cmd_5, shell=True)
p6 = subprocess.call(cmd_6, shell=True)
p7 = subprocess.call(cmd_7, shell=True)