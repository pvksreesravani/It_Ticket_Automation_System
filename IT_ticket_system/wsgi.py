import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
path = os.path.dirname(os.path.dirname(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 1. Initialize Django
application = get_wsgi_application()

# 2. FORCE the migration right now
from django.core.management import call_command
try:
    print("Running auto-migrations...")
    call_command('migrate', interactive=False)
    
    # 3. Double-check the Site table
    from django.contrib.sites.models import Site
    if not Site.objects.filter(id=1).exists():
        Site.objects.create(id=1, domain='vercel.app', name='Vercel')
        print("Site record created.")
except Exception as e:
    print(f"Migration error: {e}")

app = application