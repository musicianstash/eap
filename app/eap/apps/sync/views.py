# -*- coding: utf-8 -*-
import json

from eap.apps.sync.item import save_crawler_item
from jsonrpc import jsonrpc_method


@jsonrpc_method('crawler.add_item')
def add_item(request, item_json):
    item_data = json.loads(item_json)
    print(item_data['name'])
    # save_crawler_item.apply(item_data)
    # save_crawler_item(item_data)
    return True
