# -*- coding: utf-8 -*-
from django.contrib import admin
from suit.admin import SortableTabularInline

from .models import Crawler, CrawlerCategory

from sorl.thumbnail.admin import AdminImageMixin


class CrawlerCategoryInline(AdminImageMixin, SortableTabularInline):
    model = CrawlerCategory
    extra = 0
    sortable = 'order'


class CrawlerAdmin(admin.ModelAdmin):
    """CRAWLERS
    """
    search_fields = ('store', 'name')
    list_display = ('is_active', 'name', 'store', 'status', 'download_delay')
    list_display_links = ('name',)
    list_filter = ('is_active', 'name', 'store', 'status')
    #
    # # FORM PARAMS
    readonly_fields = ('status',)
    fieldsets = [
        (None, {'fields': [
            'name', 'store', 'is_active', 'download_delay', 'concurrent_requests'
        ]}),
    ]

    inlines = (CrawlerCategoryInline,)


admin.site.register(Crawler, CrawlerAdmin)

# -*- coding: utf-8 -*-
# from django.contrib import admin
#
# from .models import Crawler
#
# admin.site.register(Crawler)
