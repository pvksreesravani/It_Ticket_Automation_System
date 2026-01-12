import os
import time
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 1. Initialize Django
django.setup()

# 2. Force Migration and Site Creation
try:
    print("Initializing Database...")
    call_command('migrate', interactive=False)
    
    # Import inside the try block to avoid early-load crashes
    from django.contrib.sites.models import Site
    Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
    print("Database Ready.")
except Exception as e:
    print(f"Database Error: {e}")

# 3. Final Application Export
application = get_wsgi_application()
app = application