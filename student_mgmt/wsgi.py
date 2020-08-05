"""
WSGI config for student_mgmt project.

##########################################
##  Developed By:Mustafa Raad Mutashar  ##
##  mustafa.raad.7@gmail.com     2020   ##
##########################################

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_mgmt.settings')

application = get_wsgi_application()
