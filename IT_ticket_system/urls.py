from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # The ONLY admin entry you need
    path('admin/', admin.site.urls),
    
    # This sends users to the login page immediately if they visit the base URL
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    
    # This handles the Google Login AND regular login/signup
    path('accounts/', include('allauth.urls')), 
    
    # This connects to your tickets app logic
    path('tickets/', include('tickets.urls')),
]