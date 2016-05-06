# -*- coding: utf-8 -*-
from eap.apps.store.models import Store


def get_or_create_store_obj(store):
    store, created = Store.objects.get_or_create(name=store)
    return store
