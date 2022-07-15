"""
WSGI config for DjangoGameOnline project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoGameOnline.settings')

# currentpath = os.path.dirname(__file__)
# if currentpath not in sys.path:
#     sys.path.append(currentpath)
#
print('sys.path: ',sys.path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
