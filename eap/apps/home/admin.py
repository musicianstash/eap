# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Slider

from sorl.thumbnail.admin import AdminImageMixin


class SliderAdmin(AdminImageMixin, admin.ModelAdmin):
    """SLIDER
    """
    # LIST PARAMS
    search_fields = ('title',)
    list_display = ('title',)
    list_display_links = ('title',)

    # FORM PARAMS
    fieldsets = [
        (None, {
            'fields': ['is_active', 'background_type', 'image', 'caption_position']
        }),
        ('Caption', {
            'fields': ['title', 'title_type']
        }),
        ('Caption 2', {
            'fields': ['title2', 'title_type2']
        }),
        ('Caption 3', {
            'fields': ['title3', 'title_type3']
        }),
        ('Slider link', {
            'fields': ['link', 'link_title']
        })
    ]



admin.site.register(Slider, SliderAdmin)
