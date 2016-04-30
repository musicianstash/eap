from eap.settings.base import *

DEBUG = True

COMPRESS_ENABLED = False
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter'
# ]

COMPRESS_REBUILD_TIMEOUT = 1

INSTALLED_APPS += (
    'debug_toolbar',
    'haystack_panel'
)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.sql.SQLPanel',
    'haystack_panel.panel.HaystackDebugPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

THUMBNAIL_DEBUG = True

STATIC_URL = os.getenv('EAP_STATIC_URL', '/static/')
MEDIA_URL = os.getenv('EAP_MEDIA_URL', '/media/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
