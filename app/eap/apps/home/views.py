# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View

from eap.apps.localization.models import Country


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CountriesView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'countries': Country.objects.all()
        }

        return render(request, self.template_name, context=context)
