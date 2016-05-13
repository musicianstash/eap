# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType, field, FacetedSearch, RangeFacet, TermsFacet

from .models import Item


class ItemDoc(DocType):
    created_at = field.Date()
    name = field.String()
    slug = field.String()
    image = field.String()
    price = field.Float()
    sale_price = field.Float()
    search_price = field.Float()
    discount = field.Integer()
    countries = field.String(multi=True)
    in_stock = field.Boolean()
    categories = field.Integer(multi=True)
    category_id = field.Integer()
    color = field.String()
    color_id = field.Integer()
    brand = field.String()
    brand_id = field.Integer()
    store = field.String()
    store_id = field.Integer()

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
        album_doc.discount = prepare_discount(obj)
        album_doc.countries = prepare_countries(obj)
        album_doc.in_stock = obj.in_stock
        album_doc.categories = prepare_categories(obj)
        album_doc.category_id = obj.category.id
        album_doc.color = obj.color.name
        album_doc.color_id = obj.color.id
        album_doc.brand = obj.brand.name
        album_doc.brand_id = obj.brand.id
        album_doc.store = obj.store.name
        album_doc.store_id = obj.store.id
        album_doc.save()


DISCOUNT_RANGES = [
    ('10% Of or More', (10, 25)),
    ('25% Of or More', (25, 50)),
    ('50% Of or More', (50, 70)),
    ('70% Of or More', (70, 90))
]


class ItemSearch(FacetedSearch):
    doc_types = [ItemDoc, ]

    # fields that should be searched
    fields = ['name', 'description']

    facets = {
        # use bucket aggregations to define facets
        'category_ids': TermsFacet(field='categories'),
        'color_ids': TermsFacet(field='color_id'),
        'brand_ids': TermsFacet(field='brand_id'),
        'store_ids': TermsFacet(field='store_id'),
        'in_stock': TermsFacet(field='in_stock'),
        'discounts': RangeFacet(field='discount', ranges=DISCOUNT_RANGES)
    }

    def __init__(self, query=None, filters={}, process_search=None):
        self._process_search = process_search
        super(ItemSearch, self).__init__(query, filters)

    def search(self):
        # override method to add search process method
        s = super(ItemSearch, self).search()
        return self._process_search(s) if self._process_search else s


def prepare_price(obj):
    return obj.sale_price if obj.sale_price else obj.price


def prepare_discount(obj):
    discount = int(round(obj.discount))
    return discount if discount > 0 else 0


def prepare_countries(obj):
    return [country for country in obj.countries.split(',')]


def prepare_categories(obj):
    return [category.id for category in obj.category.get_ancestors(True, True)]


ItemDoc.init()
