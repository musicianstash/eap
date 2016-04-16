# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail import ImageField


class Store(models.Model):
    is_active = models.BooleanField(default=False)

    # Description fields
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    # Image field
    image = ImageField(upload_to='stores', blank=True)

    # SEO fields
    meta_keywords = models.TextField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return self.name