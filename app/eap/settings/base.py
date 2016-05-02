"""
Django settings for eap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

import os

# *** Base settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('EAP_SECRET_KEY', 'secret_key')

DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 1

# env variable to select theme template. Defaults to music.
THEME_PREFIX = os.getenv('EAP_THEME_PREFIX', 'music')

ROOT_URLCONF = 'eap.urls'


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
    'ckeditor',
    'compressor',
    'haystack',
    'jsonrpc',
    'mptt',
    'sorl.thumbnail',
    'storages',
    'smart_selects',
    'adminsortable2',
    'bootstrap3',
    'pure_pagination',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',

    # custom extensions
    'eap.extensions.elasticdjango',

    # custom apps
    'eap.apps.localization',
    'eap.apps.brand',
    'eap.apps.catalog',
    'eap.apps.store',
    'eap.apps.api',
    'eap.apps.home',
    'eap.apps.news',
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


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/{}'.format(THEME_PREFIX))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'eap.contrib.base.context_processors.item_categories',
                'eap.contrib.base.context_processors.popular_categories',
                'eap.contrib.base.context_processors.home_slides'
            ],
        },
    },
]

WSGI_APPLICATION = 'eap.wsgi.application'


# *** Custom apps settings
DISCOUNT_RANGES = (10, 20, 30, 40, 50, 70)

OPENEXCHANGERATES_API_KEY = os.getenv('EAP_OPENEXCHANGERATES_API_KEY',
                                      'cd4f8092337f41b8a12da232d1191317')

# Elasticsearch search engine connections
ELASTICDJANGO_CONNECTIONS = {
    'default': {
        'hosts': 'elasticsearch:9200'
    },
}

ELASTICDJANGO_INDEX = 'eap'

ELASTICDJANGO_INDEX_SETTINGS = {
    'number_of_shards': 1,
    'number_of_replicas': 0,
}


# *** Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('EAP_DB_DEFAULT_NAME', 'eap'),
        'USER': os.getenv('EAP_DB_DEFAULT_USER', 'eap'),
        'PASSWORD': os.getenv('EAP_DB_DEFAULT_PASSWORD', 'eap'),
        'HOST': os.getenv('EAP_DB_DEFAULT_HOST', 'localhost'),
        'PORT': os.getenv('EAP_DB_DEFAULT_PORT', '5432'),
    }
}


# *** Cache
# https://docs.djangoproject.com/en/dev/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# *** Haystack search engine
# http://django-haystack.readthedocs.org/en/latest/toc.html
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': os.getenv('EAP_HC_DEFAULT_URL', 'http://localhost:8080/solr')
    },
}


# *** Auth
# https://docs.djangoproject.com/es/1.9/topics/auth/customizing/
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


# *** Django all auth
# http://django-allauth.readthedocs.io/en/latest/index.html
ACCOUNT_LOGOUT_ON_GET = True


# Django Suit Admin configuration
# *** http://django-suit.readthedocs.org/en/develop/configuration.html
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'EAP ADMIN',

    # menu
    'SEARCH_URL': '/admin/catalog/item/',
}


# *** Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# *** Django pure pagination
# https://github.com/jamespacileo/django-pure-pagination
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}


# *** Celery
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
BROKER_URL = os.getenv('EAP_CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.getenv('EAP_CELERY_RESULT_BACKEND', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('EAP_CELERY_TIMEZONE', 'Africa/Nairobi')


# *** CKEditor
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


# *** Solr thumbnail
# http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html
THUMBNAIL_DUMMY = True
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = 'redis'


# *** Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.getenv('EAP_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
STATIC_ROOT = os.getenv('EAP_STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATICFILES_DIRS = (
    (THEME_PREFIX, os.path.join(BASE_DIR, 'templates/{}/static'.format(THEME_PREFIX))),
)


# *** AWS Storage for static and media files (CSS, JavaScript, Images)
# http://django-storages.readthedocs.io/en/latest/
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
STATICFILES_STORAGE = 'eap.contrib.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'eap.contrib.custom_storages.MediaStorage'
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

AWS_STATIC_STORAGE_BUCKET_NAME = 'static.musicianstash.com'
AWS_MEDIA_STORAGE_BUCKET_NAME = 'media.musicianstash.com'
AWS_S3_STATIC_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STATIC_STORAGE_BUCKET_NAME)
AWS_S3_MEDIA_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_MEDIA_STORAGE_BUCKET_NAME)
STATIC_URL = "http://{}/".format(AWS_S3_STATIC_CUSTOM_DOMAIN)
MEDIA_URL = "http://{}/".format(AWS_S3_MEDIA_CUSTOM_DOMAIN)

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'

# do not use query string authentication
AWS_QUERYSTRING_AUTH = False

# disable https for cross site problems
AWS_S3_SECURE_URLS = False
AWS_PRELOAD_METADATA = True
