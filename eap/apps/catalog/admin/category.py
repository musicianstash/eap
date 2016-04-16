# -*- coding: utf-8 -*-
from django.contrib import admin
from eap.contrib.admin import SortableMPTTModelAdmin

from ..models import Category

from sorl.thumbnail.admin import AdminImageMixin


class CategoryAdmin(AdminImageMixin, SortableMPTTModelAdmin):
    """ITEM CATEGORIES

    Using Django-mptt for tree structure
        https://github.com/django-mptt/django-mptt/
    """
    # LIST PARAMS
    mptt_level_indent = 20
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'is_active', 'is_popular')
    list_display_links = ('name',)
    sortable = 'order'

    # FORM PARAMS
    fieldsets = [
        ('General Data', {
            'fields': [('name', 'slug'), 'parent', ('is_active', 'is_popular'), ('image', 'description')]
        }),
        ('SEO Keywords', {
            'fields': [('meta_keywords', 'meta_description')]
        }),
        ('Classification Keywords', {
            'fields': ['keywords']
        })
    ]


admin.site.register(Category, CategoryAdmin)
