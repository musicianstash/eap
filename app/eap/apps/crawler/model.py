# -*- coding: utf-8 -*-
from django.db import models
from eap.apps.store.models import Store


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
