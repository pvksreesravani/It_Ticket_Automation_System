import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_ticket_system.settings')

# 1. Initialize the application
application = get_wsgi_application()

# 2. Run migrations and create Site record ONLY if on Vercel
if 'VERCEL' in os.environ:
    from django.core.management import call_command
    try:
        # Create tables in RAM
        call_command('migrate', interactive=False)
        
        # Create the missing Site entry now that apps are ready
        from django.contrib.sites.models import Site
        Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})
    except Exception as e:
        print(f"Startup setup error: {e}")

app = application