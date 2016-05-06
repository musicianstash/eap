# -*- coding: utf-8 -*-
from eap.apps.catalog.models import ColorKey


def get_color_obj_from_color_name(color):
    color_options = ColorKey.objects.all()
    spider_color = color.lower()

    # attempt to check if given color matches any of the given color in the database
    for color_option in color_options:
        color_value = color_option.value.lower()

        if spider_color in color_value:
            return color_option.color

    # attempt to check if any of the colors in the database has the value in the given color text
    for color_option in color_options:
        color_value = color_option.value.lower()

        if color_value in spider_color:
            return color_option.color

    return None


def get_color_id_from_color_name(color):
    color_obj = get_color_obj_from_color_name(color)
    return color_obj.id if color_obj else None
