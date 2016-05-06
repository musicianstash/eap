# -*- coding: utf-8 -*-
from django.utils.text import slugify


def create_url_slug(brand, name, color):
    slug_params = [
        brand.strip().lower(),
        color.strip().lower(),
        name.strip().lower()
    ]
    return slugify(' '.join(slug_params))
