import os
import sys
from django.core.wsgi import get_wsgi_application

# 1. Setup path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 2. Get the application first (this handles the core setup)
application = get_wsgi_application()

# 3. Try the database setup AFTER the application is ready
try:
    from django.core.management import call_command
    from django.contrib.sites.models import Site
    
    # Run migrations and create the Site record
    call_command('migrate', interactive=False)
    Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
except Exception as e:
    print(f"Post-startup setup skipped or failed: {e}")

app = application