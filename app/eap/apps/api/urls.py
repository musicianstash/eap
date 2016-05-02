# -*- coding: utf-8 -*-
from jsonrpc import jsonrpc_site
from django.conf.urls import url
from . import views  # noqa

urlpatterns = [
    url(r'^$', jsonrpc_site.dispatch, name="jsonrpc_mountpoint"),
]
