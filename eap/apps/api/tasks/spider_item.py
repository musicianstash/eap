# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.text import slugify

from eap.apps.brand.models import Brand
from eap.apps.catalog.models import Category, ColorKey, Item, ItemImage
from eap.apps.localization.conversion import convert_value
from eap.apps.store.models import Store

import requests


logger = get_task_logger(__name__)


# @shared_task(name='save_spider_item')
def save_spider_item(item_data):
    """sends an email when feedback form is filled successfully"""
    logger.info('Processing spider item!')

    store = get_or_create_store(item_data['store'])
    brand = get_spider_item_brand_id_from_brand_name(item_data['brand'])
    color = get_spider_item_color_id_from_color_name(item_data['color'])
    category = get_spider_item_category_id_from_classifiers(item_data['classifiers'])

    item = get_or_create_item(item_data['code'])
    item.store = store
    item.brand = brand
    item.color = color
    item.category = category
    item.slug = create_url_slug(brand.name, color.name, item_data['name'])
    item.name = item_data['name'].strip()
    item.description = item_data['description'].strip()
    item.url = item_data['url'].strip()
    item.price = convert_value(item_data['price'], item_data['currency'], 'USD')
    item.sale_price = convert_value(item_data['sale_price'], item_data['currency'], 'USD')
    item.in_stock = item_data['stock']
    item.save()

    save_spider_item_images_from_image_urls(item, item_data['images'])

    logger.info('Spider item with id: {} saved!'.format(item.id))


def get_or_create_item(code):
    try:
        # item already exists
        return Item.objects.get(spider_code=code)
    except:
        return Item(spider_code=code)


def create_url_slug(brand, name, color):
    slug_params = [
        brand.strip().lower(),
        color.strip().lower(),
        name.strip().lower()
    ]
    return slugify(' '.join(slug_params))


def get_or_create_store(store):
    store, created = Store.objects.get_or_create(name=store)
    return store


def get_spider_item_category_id_from_classifiers(classifiers):
    categories = Category.objects.all()
    matched_categories = {}

    for category in categories:
        if not category.keywords:
            continue

        keywords = [k.lower().strip() for k in category.keywords.split(',') if k.strip()]
        dashed_keywords = ['-'.join(k.split(' ')) for k in keywords if len(k.split(' ')) > 1]
        keywords = dashed_keywords + keywords

        matches = 0
        for classifier in classifiers:
            classifier = classifier.lower().strip()

            if not classifier:
                continue

            for keyword in keywords:
                if keyword in classifier:
                    matches += 1

        if matches:
            matched_categories[matches] = category.id

    if not matched_categories:
        return None

    max_match_count = max(matched_categories.keys(), key=int)
    category_id = matched_categories[max_match_count]
    return Category.objects.get(id=category_id)


def get_spider_item_brand_id_from_brand_name(brand):
    return Brand.objects.get(name__istartswith=brand)


def get_spider_item_color_id_from_color_name(color):
    color_options = ColorKey.objects.all()
    spider_color = color.lower()

    # attempt to check if given color matches any of the given color in the database
    for color_option in color_options:
        color_value = color_option.value.lower()

        if spider_color in color_value:
            return color_option.color

    # attempt to check if any of the colors in the database has the value in the given color text
    for color_option in color_options:
        color_value = color_option.value.lower()

        if color_value in spider_color:
            return color_option.color

    return None


def save_spider_item_images_from_image_urls(item, image_urls):
    for image_url in image_urls:
        filename = os.path.basename(urlparse(image_url).path)
        response = requests.get(image_url)

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(response.content)
        img_temp.flush()

        django_file = File(img_temp)

        item_image = ItemImage()
        item_image.item = item
        item_image.image.save(filename, django_file)
        item.images.add(item_image)
