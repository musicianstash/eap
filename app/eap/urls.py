"""eap URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import serve


urlpatterns = [
    # administration
    url(r'^admin/', include(admin.site.urls)),
    # used by django-allauth
    url(r'^accounts/', include('allauth.urls')),
    # used by smart select plugin
    url(r'^chaining/', include('smart_selects.urls')),
    # used by custom apps
    # url(r'^account/', include('eap.apps.account.urls')),
    url(r'^catalog/', include('eap.apps.catalog.urls')),
    url(r'^news/', include('eap.apps.news.urls')),
    url(r'^apiv1/', include('eap.apps.api.urls')),

    url(r'^', include('eap.apps.home.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
    ]
