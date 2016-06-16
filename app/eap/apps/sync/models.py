# -*- coding: utf-8 -*-
from django.db import models
from eap.apps.store.models import Store
from mptt.fields import TreeForeignKey

from ..brand.models import Brand
from ..catalog.models import Category

CRAWLER_STATUS_CHOICES = ((1, 'Not Running'), (2, 'Queue'), (3, 'Running'), (4, 'Stopping'))


class Crawler(models.Model):
    is_active = models.BooleanField(default=False)
    status = models.SmallIntegerField(choices=CRAWLER_STATUS_CHOICES, default=1)
    store = models.ForeignKey(Store)

    name = models.CharField(max_length=64)
    download_delay = models.FloatField(default=0)
    concurrent_requests = models.FloatField(default=8)

    def __str__(self):
        return self.name


class CrawlerCategory(models.Model):
    crawler = models.ForeignKey(Crawler, related_name='categories')
    category = TreeForeignKey(Category)
    classifier = models.BooleanField(default=True)
    name = models.BooleanField(default=False)
    description = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, null=True)
    keys = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
