# -*- coding: utf-8 -*-
from django.contrib import admin
from suit.admin import SortableTabularInline

from eap.apps.catalog.models import Item, ItemImage

from sorl.thumbnail.admin import AdminImageMixin


class ItemImageInline(AdminImageMixin, SortableTabularInline):
    model = ItemImage
    extra = 0
    sortable = 'order'
    readonly_fields = ('hash_tag',)


class ItemAdmin(admin.ModelAdmin):
    """ITEMS
    """
    search_fields = ('name', 'slug', 'spider_code')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'brand', 'store', 'color', 'price',
                    'sale_price', 'spider_code', 'in_stock')
    list_display_links = ('name',)
    list_filter = ('status', 'brand', 'store', 'category', 'color', 'in_stock')

    # FORM PARAMS
    fieldsets = [
        ('General Data', {
            'fields': [('status', 'type'), ('category', 'brand', 'store'),
                       ('name', 'slug'), ('price', 'sale_price'),
                       ('in_stock', 'color'), 'description', 'countries']
        }),
        ('Retailer urls', {
            'fields': ['url', 'affiliate_url']
        }),
    ]

    inlines = (ItemImageInline,)


admin.site.register(Item, ItemAdmin)
