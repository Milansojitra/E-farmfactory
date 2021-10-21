
import os
import socket
socket.getaddrinfo('localhost', 8000)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'efarmfactory.settings')

application = get_wsgi_application()
