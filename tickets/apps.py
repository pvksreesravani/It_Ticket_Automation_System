import os
from django.apps import AppConfig

class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickets'

    def ready(self):
        # Only run this on Vercel
        if 'VERCEL' in os.environ:
            from django.core.management import call_command
            try:
                # This forces tables to be created BEFORE the site loads
                call_command('migrate', interactive=False)
                
                # This creates the missing 'django_site' table entry
                from django.contrib.sites.models import Site
                Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'IT Ticket System'})
            except Exception:
                pass