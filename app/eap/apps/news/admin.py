# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from suit.admin import SortableModelAdmin, ModelAdmin
from suit.widgets import SuitSplitDateTimeWidget
from .models import Article, ArticleCategory, ArticleImage, Subscriber
from ckeditor.widgets import CKEditorWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content': CKEditorWidget,
            'published_at': SuitSplitDateTimeWidget,
            'created_at': SuitSplitDateTimeWidget,
            'updated_at': SuitSplitDateTimeWidget,
        }
        fields = ['title', 'slug', 'content', 'excerpt', 'category', 'publisher', 'status', 'published_at']


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class ArticleAdmin(SortableModelAdmin):
    inlines = (ArticleImageInline,)
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.HORIZONTAL}
    sortable = 'order'


class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleCategoryAdmin(SortableModelAdmin):
    form = ArticleCategoryForm
    sortable = 'order'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


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

