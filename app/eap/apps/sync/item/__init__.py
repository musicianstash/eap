# -*- coding: utf-8 -*-
from eap.apps.catalog.models import Item
from eap.apps.localization.conversion import convert_value
from .brand import get_brand_id_from_brand_name
from .category import get_category_from_category_name
from .color import get_color_obj_from_color_name
from .image import save_item_images_from_image_urls
from .store import get_or_create_store_obj
from ..utils import create_url_slug


# @shared_task(name='save_crawler_item')
def save_crawler_item(item_data):
    """sends an email when feedback form is filled successfully"""
    store_obj = get_or_create_store_obj(item_data['store'])
    brand_obj = get_brand_id_from_brand_name(item_data['brand'])
    color_obj = get_color_obj_from_color_name(item_data['color'])
    category_obj = get_category_from_category_name(item_data['classifiers'])

    item, is_new = get_or_create_item(item_data['unique_code'])
    item.type = 2
    item.status = 2 if store_obj and brand_obj and color_obj else 1
    item.store = store_obj
    item.brand = brand_obj
    item.color = color_obj
    item.category = category_obj
    item.name = item_data['name'].strip()
    item.description = item_data['description'].strip()
    item.url = item_data['url'].strip()
    item.price = convert_value(item_data['price'], item_data['currency'], 'USD')
    item.sale_price = convert_value(item_data['sale_price'], item_data['currency'], 'USD')
    item.in_stock = item_data['stock']
    item.countries = ','.join(item_data['countries'])

    item.slug = create_url_slug(
        brand_obj.name,
        color_obj.name if color_obj else '',
        item_data['name']
    )
    item.save()

    if is_new:
        save_item_images_from_image_urls(item, item_data['images'])


def get_or_create_item(code):
    try:
        # item already exists
        return Item.objects.get(code=code), False
    except:
        return Item(code=code), True
