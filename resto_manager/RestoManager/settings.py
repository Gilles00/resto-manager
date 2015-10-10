

"""
Django settings for RestoManager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vby9-$dy1k+r#4tbm1-=5yxu@vz3&=!60#07gb4f%91$_et6mh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True

SESSION_SAVE_EVERY_REQUEST = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.core.mail',
    'restaurants',
    'comptes',
    'notifications',
    'directions',
	'south',
	'reversion',
	'commandes',
	'livreurs',
    'twilio',
)

AUTH_PROFILE_MODULE = "comptes.UserProfile"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
	'django.core.context_processors.request',
)

ROOT_URLCONF = 'RestoManager.urls'

WSGI_APPLICATION = 'RestoManager.wsgi.application'

# Email configuration.
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'etsrestomanager@gmail.com'
EMAIL_HOST_PASSWORD = 'etslog210'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'etsrestomanager@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



# Databasejj
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resto_manager',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates')

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static"),
)

TWILIO_ACCOUNT_SID = 'AC50f3d1912a72cd316697a0e4482b69bd'
TWILIO_AUTH_TOKEN = 'd65099e18390a7398b7878ea262d5108'

