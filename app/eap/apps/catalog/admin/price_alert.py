# -*- coding: utf-8 -*-
from django.contrib import admin
from ..models import PriceAlert


admin.site.register(PriceAlert, admin.ModelAdmin)
