# -*- coding: utf-8 -*-
from django.conf import settings

from elasticsearch_dsl import DocType, field

from .models import Item


class ItemDoc(DocType):
    created_at = field.Date()
    name = field.String()
    slug = field.String()
    image = field.String()
    price = field.Float()
    sale_price = field.Float()
    search_price = field.Float()
    rounder_discount = field.Integer()
    countries = field.String(multi=True)
    in_stock = field.Boolean()
    categories = field.String(multi=True)
    category_slug = field.String()
    color = field.String()
    brand = field.String()
    store = field.String()

    class Meta:
        index = 'eapitem'
        doc_type = 'item'

    def get_model_obj(self):
        return Item.objects.get(id=self.meta.id)

    @classmethod
    def sync_index(cls):
        for model in Item.objects.all().iterator():
            cls.sync(model)

    @classmethod
    def sync(cls, obj):
        album_doc = ItemDoc(meta={'id': obj.id})
        album_doc.name = obj.name
        album_doc.slug = obj.slug
        album_doc.image = obj.image.path
        album_doc.price = obj.price
        album_doc.sale_price = obj.sale_price
        album_doc.search_price = prepare_price(obj)
        album_doc.rounder_discount = prepare_rounded_discount(obj)
        album_doc.countries = prepare_countries(obj)
        album_doc.in_stock = obj.in_stock
        album_doc.categories = prepare_categories(obj)
        album_doc.category_slug = obj.category.slug or 'unknown'
        album_doc.color = obj.color.name
        album_doc.brand = obj.brand.name
        album_doc.store = obj.store.name
        album_doc.save()


def prepare_price(obj):
    return obj.sale_price if obj.sale_price else obj.price


def prepare_rounded_discount(obj):
    rounded_discount = int(round(obj.discount - 5, -1))

    if rounded_discount > 0 and rounded_discount in settings.DISCOUNT_RANGES:
        return rounded_discount

    return 0


def prepare_countries(obj):
    return [country for country in obj.countries.split(',')]


def prepare_categories(obj):
    return [category.slug for category in obj.category.get_ancestors(True, True)]


ItemDoc.init()
