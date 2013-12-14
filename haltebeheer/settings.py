"""
Django settings for haltebeheer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g1(cvpvtvr4iigcu1@4^7s172)&_&1a4b#y)%(8^3iue5_-gwi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    "haltebeheer/templates",
)


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # Our apps
    'stopmanagement',

    # Libs
    'leaflet',
    'south',
    'floppyforms',
    'crispy_forms',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'haltebeheer.urls'

WSGI_APPLICATION = 'haltebeheer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '',
        'NAME': 'haltebeheer',
        'USER': 'haltebeheer',
        'PASSWORD': 'Duttec90',
        'SCHEMA': 'public',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    'stopmanagement/locale',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    "haltebeheer/static",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Configure the leaflet maps
LEAFLET_CONFIG = {
    # 53.554260, 7.227610, 50.750450, 3.358330
    'SPATIAL_EXTENT': (7.227610, 53.554260, 3.358330, 50.750450),
    'PLUGINS': {
        'geosearch': {
            'css': 'css/l.geosearch.css',
            'js': ['js/l.control.geosearch.js', 'js/l.geosearch.provider.openstreetmap.js'],
            'auto-include': False,
        },
        'sidebar': {
            'css': 'css/L.Control.Sidebar.css',
            'js': 'js/L.Control.Sidebar.js',
            'auto-include': False,
        },
    }
}
