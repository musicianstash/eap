# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Brand, BrandKey

from sorl.thumbnail.admin import AdminImageMixin


class BrandKeyInline(admin.TabularInline):
    model = BrandKey
    fields = ('value',)
    extra = 1
    verbose_name_plural = 'Brand Keys / Values'


class BrandAdmin(AdminImageMixin, admin.ModelAdmin):
    """ITEM BRANDS
    """
    # LIST PARAMS
    search_fields = ('name', 'slug')
    list_display = ('name', 'is_active', 'is_popular')
    list_display_links = ('name',)
    list_filter = ('is_active', 'is_popular')
    ordering = ['name']

    # FORM PARAMS
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['is_active', 'is_popular', ('name', 'slug'), 'image', 'description']
        }),

        ('SEO Keywords', {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ['meta_keywords', 'meta_description']
        })
    ]

    prepopulated_fields = {'slug': ('name',)}

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO Data'))

    inlines = (BrandKeyInline,)

admin.site.register(Brand, BrandAdmin)
