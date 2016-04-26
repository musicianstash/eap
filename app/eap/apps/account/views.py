from django.core.context_processors import csrf
from django.views.generic import View
from django.http import *
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


class ProfileView(View):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))
        return render(request, self.template_name, context=context)
