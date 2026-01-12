import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# Initialize Django so we can use models
django.setup()

# Build the database in RAM immediately
try:
    call_command('migrate', interactive=False)
    from django.contrib.sites.models import Site
    Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
except Exception as e:
    print(f"Startup Database Error: {e}")

# Create the final application object for Vercel
application = get_wsgi_application()
app = application