# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Country, Currency, ExchangeRate

admin.site.register(ExchangeRate)
admin.site.register(Country, admin.ModelAdmin)
admin.site.register(Currency, admin.ModelAdmin)
