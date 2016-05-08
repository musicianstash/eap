# -*- coding: utf-8 -*-
from .models import Article

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

from pure_pagination.mixins import PaginationMixin


class ArticleView(View):
    template_name = 'news/article.html'

    def get(self, request, slug):
        context = {
            'article': Article.objects.get(slug=slug),
            'recommended_articles': Article.objects.all()[:4]
        }

        return render(request, self.template_name, context=context)


class ArticlesListView(PaginationMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'news/articles.html'
    paginate_by = 10