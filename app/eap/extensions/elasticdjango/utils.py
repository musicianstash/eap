
from pyclbr import readmodule

import inspect

from django.apps import apps
from django.utils.module_loading import import_string

from elasticsearch_dsl import DocType


def load_documents(app_name=None, document=None):
    document_instances = []

    for app in apps.get_app_configs():
        if app_name and app_name != app.name:
            continue

        module_path = '{}.documents'.format(app.name)

        if not module_exists(module_path):
            continue

        for class_name, module_class in readmodule(module_path).items():
            document_path = '{}.{}'.format(module_path, class_name)
            document_class = import_string(document_path)

            if not issubclass(document_class, DocType):
                continue

            document_instances.append(document_class)

    return document_instances


def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True
