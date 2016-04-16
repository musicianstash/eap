# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from eap.apps.api.tasks import save_spider_item

import simplejson


class ItemView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ItemView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        item_data = simplejson.loads(request.body)
        # save_spider_item.apply(item_data)
        save_spider_item(item_data)
        return JsonResponse({'success': True})
