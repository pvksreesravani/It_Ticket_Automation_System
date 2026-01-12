
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# Migration trick
os.system("python manage.py migrate --noinput")

application = get_wsgi_application()
app = application