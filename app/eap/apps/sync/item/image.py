# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from eap.apps.catalog.models import ItemImage

import requests


def save_item_images_from_image_urls(item, image_urls):
    for image_url in image_urls:
        django_file, filename = download_image_from_image_url(image_url)

        item_image = ItemImage()
        item_image.item = item
        item_image.image.save(filename, django_file)
        item.images.add(item_image)


def download_image_from_image_url(image_url):
    response = requests.get(image_url)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(response.content)
    img_temp.flush()

    django_file = File(img_temp)
    filename = os.path.basename(urlparse(image_url).path)

    return django_file, filename
