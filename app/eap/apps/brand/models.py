# -*- coding: utf-8 -*-
from django.db import models

from eap.contrib.models import CacheAllMixin

from sorl.thumbnail import ImageField

BRAND_CACHE_KEY = 'brand.models.brand'


class Brand(CacheAllMixin, models.Model):
    cache_all_mixin_key = BRAND_CACHE_KEY

    is_active = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    # Description fields
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    # Image field
    image = ImageField(upload_to='brands', blank=True)

    # SEO fields
    meta_keywords = models.TextField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BrandKey(models.Model):
    value = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, null=True)

    def __str__(self):
        return self.value
