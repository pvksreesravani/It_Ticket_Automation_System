import os
from pathlib import Path

# 1. BASE DIRECTORY
# This must stay at the top so other settings can use it
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. SECURITY SETTINGS
SECRET_KEY = 'django-insecure-6elc4hgz$*kdgma7(@$9r$d3(b(^(n#*13re1$6o@p8f08!h_x'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Temporarily use '*' to rule out host errors

# 3. APPLICATION DEFINITION
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Allauth & Google OAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    # Your Internal App
    'tickets.apps.TicketsConfig',
]

# Required for django-allauth
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Required for allauth
]

ROOT_URLCONF = 'IT_ticket_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django to find your base.html in the main folder
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IT_ticket_system.wsgi.application'

# 4. DATABASE
# 4. DATABASE
if 'VERCEL' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# 5. AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Traffic Controller: Where users go after login/logout
LOGIN_REDIRECT_URL = 'login_redirect'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Google OAuth Configuration
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}

# 6. PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 7. INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 8. STATIC FILES (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# This tells Django where your 'static' folder is located
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Folder where static files are collected for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 9. DEFAULT PRIMARY KEY FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Force Site ID but prevent database lookup during initialization
from django.contrib.sites.models import Site

def get_site_id():
    try:
        return Site.objects.get_or_create(id=1, defaults={'domain': 'vercel.app', 'name': 'Vercel'})[0].id
    except:
        return 1

SITE_ID = get_site_id()
# --- AT THE VERY BOTTOM OF settings.py ---

# Safe SITE_ID for Vercel In-Memory DB
if 'VERCEL' in os.environ:
    SITE_ID = 1
else:
    # On your local computer, try to get the real ID
    try:
        from django.contrib.sites.models import Site
        SITE_ID = Site.objects.get_or_create(id=1, defaults={'domain': '127.0.0.1:8000', 'name': 'Local'})[0].id
    except:
        SITE_ID = 1