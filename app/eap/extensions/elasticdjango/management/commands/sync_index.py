from django.core.management.base import BaseCommand

from eap.extensions.elasticdjango.indexer import sync_index


class Command(BaseCommand):
    es = None

    def handle(self, *args, **kwargs):
        sync_index()
