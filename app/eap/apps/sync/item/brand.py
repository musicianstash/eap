# -*- coding: utf-8 -*-
from eap.apps.brand.models import Brand


def get_brand_id_from_brand_name(brand):
    return Brand.objects.get(name__istartswith=brand)
