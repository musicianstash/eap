# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Store

from sorl.thumbnail.admin import AdminImageMixin


class StoreAdmin(AdminImageMixin, admin.ModelAdmin):
    """Stores
    """
    # LIST PARAMS
    search_fields = ('name', 'slug')
    list_display = ('name', 'is_active')
    list_display_links = ('name',)
    ordering = ['name']

    # FORM PARAMS
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['is_active', ('name', 'slug'), 'image', 'description']
        }),

        ('SEO Keywords', {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ['meta_keywords', 'meta_description']
        })
    ]

    prepopulated_fields = {'slug': ('name',)}

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO Data'))


admin.site.register(Store, StoreAdmin)
