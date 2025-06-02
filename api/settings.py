INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'product',
]

# Add CORS headers if needed for browser testing
CORS_ALLOW_ALL_ORIGINS = True  # Only for development

# Tastypie settings
TASTYPIE_DEFAULT_FORMATS = ['json']