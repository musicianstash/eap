# -*- coding: utf-8 -*-
from django.db import models

from eap.apps.brand.models import Brand
from eap.apps.localization.models import Currency
from eap.apps.store.models import Store

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from sorl.thumbnail import ImageField


class Color(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ColorKey(models.Model):
    value = models.CharField(max_length=32)
    color = models.ForeignKey(Color, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)

    def __str__(self):
        return self.value


class Category(MPTTModel):
    """Using Django-mptt for tree structure: https://github.com/django-mptt/django-mptt/
    """
    is_active = models.BooleanField()
    is_popular = models.BooleanField()

    # Description fields
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    # Image field
    image = ImageField(upload_to='categories', blank=True)

    # SEO fields
    meta_keywords = models.TextField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    keywords = models.TextField(blank=True)

    # Tree and order fields
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')
    # Sortable property
    order = models.PositiveIntegerField()

    class MPTTMeta:
        order_insertion_by = ['order']

    # It is required to rebuild tree after save, when using order for mptt-tree
    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        Category.objects.rebuild()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


ITEM_TYPE_CHOICES = ((1, 'Normal type'), (2, 'Spider type'))
ITEM_STATUS_CHOICES = ((1, 'Draft'), (2, 'Published'), (3, 'Disabled'), (4, 'Ignored'))


class Item(models.Model):
    # Type and status fields
    type = models.SmallIntegerField(choices=ITEM_TYPE_CHOICES, default=1)
    status = models.SmallIntegerField(choices=ITEM_STATUS_CHOICES, default=1)
    spider_code = models.CharField(max_length=128, blank=True)

    # Description fields
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True)
    color = models.ForeignKey(Color, null=True)

    # Designer and merchant field
    brand = models.ForeignKey(Brand)
    store = models.ForeignKey(Store)

    # Retailer url and affiliate url
    url = models.URLField(blank=True)
    affiliate_url = models.URLField(blank=True)

    # Price fields
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)

    countries = models.TextField(blank=True)

    in_stock = models.BooleanField(default=False)

    category = TreeForeignKey(Category, null=True)

    # SEO fields
    meta_keywords = models.TextField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def image(self):
        return self.images.all()[0].image

    @property
    def discount(self):
        if not self.sale_price or not self.price:
            return 0

        return int((1 - (self.sale_price / self.price)) * 100)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images')
    image = ImageField(upload_to='products')
    hash_tag = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)


class StockAlert(models.Model):
    item = models.ForeignKey(Item, related_name='stock_alert')
    email = models.EmailField(max_length=254)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_datetime',)
        unique_together = (("item", "email"),)


class PriceAlert(models.Model):
    item = models.ForeignKey(Item, related_name='price_alert')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField(max_length=254)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_datetime',)
        unique_together = (("item", "email"),)
