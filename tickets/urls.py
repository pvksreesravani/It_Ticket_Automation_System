from django.urls import path
from . import views

urlpatterns = [
    # Role-based logic (The Traffic Controller)
    path('login-check/', views.login_redirect, name='login_redirect'),

    # User Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Technician Dashboard
    path('technician/', views.technician_dashboard, name='technician_dashboard'),
    
    # Ticket Operations
    path('create/', views.create_ticket, name='create_ticket'),
    path('my-tickets/', views.my_tickets, name='my_tickets'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),
]