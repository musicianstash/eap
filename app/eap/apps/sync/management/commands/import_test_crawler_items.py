# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = 'https://www.dropbox.com/s/m0c3jwm35kmtajz/music_items.json?dl=1'
        json_text = requests.get(url)
        json_items = json.loads(json_text)

        for json_item in json_items:
            print(json_item)
