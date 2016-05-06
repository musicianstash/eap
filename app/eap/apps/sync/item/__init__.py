# -*- coding: utf-8 -*-
from celery.utils.log import get_task_logger


from eap.apps.localization.conversion import convert_value
from eap.apps.catalog.models import Item

from .brand import get_brand_id_from_brand_name
from .category import predict_category_id_from_text
from .color import get_color_obj_from_color_name
from .image import save_item_images_from_image_urls
from .store import get_or_create_store_obj

from ..utils import create_url_slug


logger = get_task_logger(__name__)


# @shared_task(name='save_crawler_item')
def save_crawler_item(item_data):
    """sends an email when feedback form is filled successfully"""
    logger.info('Processing spider item!')

    store = get_or_create_store_obj(item_data['store'])
    brand = get_brand_id_from_brand_name(item_data['brand'])
    color = get_color_obj_from_color_name(item_data['color'])
    category = predict_category_id_from_text(item_data['classifiers'])

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

    save_item_images_from_image_urls(item, item_data['images'])

    logger.info('Spider item with id: {} saved!'.format(item.id))


def get_or_create_item(code):
    try:
        # item already exists
        return Item.objects.get(spider_code=code)
    except:
        return Item(spider_code=code)

