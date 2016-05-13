# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand
from ...item import save_crawler_item

import requests


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = 'https://www.dropbox.com/s/m0c3jwm35kmtajz/music_items.json?dl=1'
        json_text = requests.get(url)
        json_items = json.loads(json_text.text)

        for json_item in json_items:
            if 'electric guitar' not in json_item['classifiers']:
                continue

            try:
                save_crawler_item(json_item)
            except:
                print("Something wrong: " + json_item['name'])
