"""
Django settings for eap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.abspath(os.path.dirname(__name__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('EAP_SECRET_KEY', 'secret_key')

DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    # admin theme app
    'suit',

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # external apps
    'compressor',
    'haystack',
    'rest_framework',
    'mptt',
    'sorl.thumbnail',
    'smart_selects',
    'adminsortable2',
    'bootstrap3',
    'pure_pagination',
    # 'turbolinks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',

    # custom apps
    'eap.apps.localization',
    'eap.apps.brand',
    'eap.apps.catalog',
    'eap.apps.store',
    'eap.apps.api',
    'eap.apps.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'turbolinks.middleware.TurbolinksMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'eap.middleware.ProcessExceptionMiddleware'
)

ROOT_URLCONF = 'eap.urls'

# env variable to select theme template. Defaults to music.
THEME_PREFIX = os.getenv('EAP_THEME_PREFIX', 'music')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'eap/templates/{}'.format(THEME_PREFIX))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'eap.contrib.base.context_processors.item_categories',
                'eap.contrib.base.context_processors.popular_categories',
                'eap.contrib.base.context_processors.home_slides'
            ],
        },
    },
]

WSGI_APPLICATION = 'eap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('EAP_DB_DEFAULT_NAME', 'eap'),
        'USER': os.getenv('EAP_DB_DEFAULT_USER', 'root'),
        'PASSWORD': os.getenv('EAP_DB_DEFAULT_PASSWORD', 'admin'),
        'HOST': os.getenv('EAP_DB_DEFAULT_HOST', 'localhost'),
        'PORT': os.getenv('EAP_DB_DEFAULT_PORT', '3306'),
    }
}

# Cache
# https://docs.djangoproject.com/en/dev/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# Haystack search engine
# http://django-haystack.readthedocs.org/en/latest/toc.html
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': os.getenv('EAP_HC_DEFAULT_URL', 'http://127.0.0.1:8080/solr')
    },
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_LOGOUT_ON_GET = True

# Django Suit Admin configuration
# http://django-suit.readthedocs.org/en/develop/configuration.html
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'EAP ADMIN',

    # menu
    'SEARCH_URL': '/admin/catalog/item/',
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DISCOUNT_RANGES = (10, 20, 30, 40, 50, 70)

OPENEXCHANGERATES_API_KEY = os.getenv('EAP_OPENEXCHANGERATES_API_KEY',
                                      'cd4f8092337f41b8a12da232d1191317')

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = os.getenv('EAP_STATIC_URL', '/static/')
MEDIA_ROOT = os.getenv('EAP_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = os.getenv('EAP_MEDIA_URL', '/media/')
STATIC_ROOT = os.getenv('EAP_STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'eap/templates/{}/static'.format(THEME_PREFIX)),
)

# Solr thumbnail
# http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html
THUMBNAIL_DUMMY = True

# Celery
BROKER_URL = os.getenv('EAP_CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.getenv('EAP_CELERY_RESULT_BACKEND', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
