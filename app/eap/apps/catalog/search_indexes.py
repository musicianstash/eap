# -*- coding: utf-8 -*-
# import datetime
# from django.conf import settings
#
# from haystack import indexes
#
# from .models import Item
#
#
# class ItemIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     name = indexes.CharField(model_attr='name')
#     slug = indexes.CharField(model_attr='slug')
#     description = indexes.CharField(model_attr='description')
#     image = indexes.CharField(model_attr='image__path')
#     original_price = indexes.DecimalField(model_attr='price')
#     sale_price = indexes.DecimalField(model_attr='sale_price')
#     price = indexes.DecimalField()
#     discount = indexes.IntegerField(model_attr='discount')
#     rounded_discount = indexes.FacetIntegerField()
#     countries = indexes.MultiValueField()
#     in_stock = indexes.FacetBooleanField(model_attr='in_stock')
#     categories = indexes.FacetMultiValueField()
#     category_slug = indexes.FacetCharField(model_attr='category__slug', default='unknown')
#     color = indexes.FacetCharField(model_attr='color')
#     brand = indexes.FacetCharField(model_attr='brand')
#     store = indexes.FacetCharField(model_attr='store')
#
#     def get_model(self):
#         return Item
#
#     def prepare_price(self, obj):
#         return obj.sale_price if obj.sale_price else obj.price
#
#     def prepare_rounded_discount(self, obj):
#         rounded_discount = int(round(obj.discount - 5, -1))
#
#         if rounded_discount > 0 and rounded_discount in settings.DISCOUNT_RANGES:
#             return rounded_discount
#
#         return 0
#
#     def prepare_countries(self, obj):
#         return [country for country in obj.countries.split(',')]
#
#     def prepare_categories(self, obj):
#         return [category.slug for category in obj.category.get_ancestors(True, True)]
#
#     # def index_queryset(self, using=None):
#     #     """Used when the entire index for model is updated."""
#     #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
