import os
import sys
from django.core.wsgi import get_wsgi_application

# 1. Setup path and environment
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 2. Force Database Setup on every startup
import django
django.setup()

from django.core.management import call_command
from django.contrib.sites.models import Site

try:
    # Build the tables in RAM
    call_command('migrate', interactive=False)
    
    # Create the 'Site' record that django-allauth requires
    # This prevents the 500 error on the login page
    Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
    print("Database migrated and Site record created successfully.")
except Exception as e:
    print(f"Startup error: {e}")

application = get_wsgi_application()
app = application