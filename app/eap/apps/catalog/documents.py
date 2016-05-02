# -*- coding: utf-8 -*-
from eap.extensions.elasticdjango.document import Document, field

from .models import Item


class ItemDoc(Document):
    created_at = field.Date()
    name = field.String()
    slug = field.String()
    description = field.String()
    image = field.String()
    original_price = field.Float()
    sale_price = field.Float()
    price = field.Float()
    rounder_discount = field.Integer()
    countries = field.String(multi=True)
    in_stock = field.Boolean()
    categories = field.String(multi=True)
    category_slug = field.String()
    color = field.String()
    brand = field.String()
    store = field.String()

    class Meta:
        index = 'eap_item'
        doc_type = 'item'
    #
    # @classmethod
    # def sync(cls, item):
    #     album_doc = ItemDoc(meta={'id': item.id})
    #     album_doc.name = item.name
    #     album_doc.slug = item.slug
    #     album_doc.description = item.description
    #     album_doc.save()
    #
    # def save(self, *args, **kwargs):
    #     return super(ItemDoc, self).save(*args, **kwargs)
    #
    # def get_model_obj(self):
    #     return Item.objects.get(id=self.meta.id)
