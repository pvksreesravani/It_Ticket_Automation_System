import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 1. Initialize Django
application = get_wsgi_application()

# 2. FORCE the migration
from django.core.management import call_command
try:
    # Use interactive=False instead of --noinput
    call_command('migrate', interactive=False)
    
    # 3. Create Site record
    from django.contrib.sites.models import Site
    Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
except Exception as e:
    print(f"Migration check: {e}")

app = application