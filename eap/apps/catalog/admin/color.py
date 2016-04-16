# -*- coding: utf-8 -*-
from django.contrib import admin
from suit.admin import SortableTabularInline


from ..models import Color, ColorKey


class ColorKeyInline(SortableTabularInline):
    model = ColorKey
    fields = ('value',)
    extra = 1
    verbose_name_plural = 'Color Keys / Values'
    sortable = 'order'


class ColorAdmin(admin.ModelAdmin):
    """ATTRIBUTE GROUPS
    """
    # LIST PARAMS
    search_fields = ('name',)
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']

    inlines = (ColorKeyInline,)


admin.site.register(Color, ColorAdmin)
