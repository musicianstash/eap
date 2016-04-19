# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from suit.admin import SortableModelAdmin
from suit.widgets import SuitSplitDateTimeWidget
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content': forms.TextInput(),
            # 'category':
            'published_date': SuitSplitDateTimeWidget,
            'created_date': SuitSplitDateTimeWidget,
            'updated_date': SuitSplitDateTimeWidget,
            # 'reporter': forms.
            # 'images':
        }


class ArticleAdmin(SortableModelAdmin):
    form = ArticleForm
    sortable = 'order'

admin.site.register(Article, ArticleAdmin)