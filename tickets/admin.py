from django.contrib import admin
from .models import Ticket # This looks into models.py for the Ticket class

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'assigned_to', 'status', 'priority')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)

    fieldsets = (
        ('Info', {'fields': ('title', 'description', 'user')}),
        ('Status', {'fields': ('category', 'priority', 'status')}),
        ('Assignment', {'fields': ('assigned_to',)}),
    )

    # Logic: Technicians only see tickets assigned to them
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Technician').exists():
            return qs.filter(assigned_to=request.user)
        return qs

    # Logic: Technicians cannot edit the title or description
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Technician').exists():
            return ('title', 'description', 'user', 'category', 'priority', 'assigned_to')
        return []