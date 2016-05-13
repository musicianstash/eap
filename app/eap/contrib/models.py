# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class CacheAllMixin(object):
    cache_all_mixin_key = None

    @classmethod
    def cached_objects(cls):
        objects = cache.get(cls.cache_all_mixin_key)

        if not objects:
            objects = cls.objects.all()
            cache.add(cls.cache_all_mixin_key, objects, 24 * 60 * 60)

        return objects

    @classmethod
    def cached_names(cls):
        objects = {}
        for model_object in cls.cached_objects():
            objects[model_object.id] = model_object.name
        return objects


@receiver([pre_save, post_delete])
def cache_mixin_model_handler(sender, **kwargs):
    if hasattr(sender, 'cache_all_mixin_key'):
        cache.delete(sender.cache_mixin_key)
