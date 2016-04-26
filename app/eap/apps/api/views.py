# -*- coding: utf-8 -*-
from eap.apps.api.tasks import save_spider_item
from jsonrpc import jsonrpc_method


@jsonrpc_method('crawler.test_item')
def test_item(request, item):
    return 'Test item works! {}'.format(item['name'])


@jsonrpc_method('crawler.add_item')
def add_item(request, item_data):
    # save_spider_item.apply(item_data)
    save_spider_item(item_data)
    return 'Successfully updated!'
