# -*- coding: utf-8 -*-
from django.contrib import admin

from suit.admin import SortableModelAdmin, ModelAdmin
from .models import Article, ArticleCategory, ArticleImage, Subscriber
from .forms import ArticleForm, ArticleCategoryForm, SubscriberForm


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class ArticleAdmin(SortableModelAdmin):
    inlines = (ArticleImageInline,)
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.HORIZONTAL}
    sortable = 'order'


class ArticleCategoryAdmin(SortableModelAdmin):
    form = ArticleCategoryForm
    sortable = 'order'


class SubscriberAdmin(ModelAdmin):
    form = SubscriberForm
    fieldsets = [
        (None, {
            'fields': ['user', 'email', 'subscribed']}),
        ('Groups', {
            'description': 'Groups user is subscribed to',
            'fields': ['latest_news', 'new_product', 'offer']}),
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

