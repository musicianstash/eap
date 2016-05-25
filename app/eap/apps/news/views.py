# -*- coding: utf-8 -*-
from .models import Article
from .forms import SubscriberForm

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from pure_pagination.mixins import PaginationMixin


class SubscriberView(FormView):
    form_class = SubscriberForm
    success_url = '/subscribed/'

    # def get_subscriber(request):
    #     if request.method == 'POST':
    #         form = SubscriberForm(request.POST)
    #         if form.is_valid():
    #             todo: process the data in form.cleaned_data
                # pass


class ArticleView(View):
    template_name = 'news/article.html'

    def get(self, request, slug):
        context = {
            'article': Article.objects.get(slug=slug),
            'recommended_articles': Article.objects.all()[:4]
        }

        return render(request, self.template_name, context=context)


class ArticlesListView(PaginationMixin, ListView, SubscriberView):
    model = Article
    context_object_name = 'articles'
    template_name = 'news/articles.html'
    paginate_by = 10

    # def post(self, request):
    #     return SubscriberView.as_view(request)