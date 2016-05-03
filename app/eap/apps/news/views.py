# -*- coding: utf-8 -*-
from .models import Article

from django.shortcuts import render
from django.views.generic import View

from django.views.generic.list import MultipleObjectMixin


class ArticleView(View):
    template_name = 'news/article.html'

    def get(self, request, slug):
        context = {
            'article': Article.objects.get(slug=slug)
        }

        return render(request, self.template_name, context=context)


class ArticlesView(MultipleObjectMixin, View):
    template_name = 'news/articles.html'

    def get(self, request):
        return render(request, self.template_name, context={})