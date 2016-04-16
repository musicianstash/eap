# -*- coding: utf-8 -*-
from django.contrib import admin
from ..models import StockAlert


admin.site.register(StockAlert, admin.ModelAdmin)
