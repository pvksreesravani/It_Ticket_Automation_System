import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# This line tells Vercel to build your database tables on startup
os.system("python manage.py migrate")

application = get_wsgi_application()
app = application
