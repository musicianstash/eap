# -*- coding: utf-8 -*-
import json

from eap.apps.api.tasks import save_spider_item
from jsonrpc import jsonrpc_method


@jsonrpc_method('crawler.add_item')
def add_item(request, item_json):
    item_data = json.loads(item_json)
    print(item_data['name'])
    # save_spider_item.apply(item_data)
    # save_spider_item(item_data)
    return True
