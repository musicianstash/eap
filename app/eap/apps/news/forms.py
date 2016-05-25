# -*- coding: utf-8 -*-
from django import forms
from .models import Article, ArticleCategory, Subscriber
from suit.widgets import SuitSplitDateTimeWidget
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


class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'