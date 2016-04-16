# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^item/', views.ItemView.as_view(), name="api_item"),
]
