from eap.settings.base import *

DEBUG = True

COMPRESS_ENABLED = False
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter'
# ]

COMPRESS_REBUILD_TIMEOUT = 1

INSTALLED_APPS += (
    # 'debug_toolbar',
    # 'elastic_panel'
)


# Please note that more the options are enabled then slower applications will be because certain
# functionality has to wait for response to complete in order to process the data! If testing the
# response is needed then it's better to comment out functionality that you don't need!
DEBUG_TOOLBAR_PANELS = [
    'elastic_panel.panel.ElasticDebugPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    # we need to set that because otherwise debug toolbar is not working
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}


THUMBNAIL_DEBUG = True

STATIC_URL = os.getenv('EAP_STATIC_URL', '/static/')
MEDIA_URL = os.getenv('EAP_MEDIA_URL', '/media/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

TEST_CRAWL_DATA = {
    'guitars': 'https://www.dropbox.com/s/v6gkp3zf0we4z0a/music_items.json?dl=1'
}
