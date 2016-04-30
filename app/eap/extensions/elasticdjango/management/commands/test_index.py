from django.core.management.base import BaseCommand

from eap.apps.localization.documents import CurrencyDoc, CurrencySearch


class Command(BaseCommand):
    es = None

    def handle(self, *args, **kwargs):
        results = CurrencySearch().search().execute()

        for result in results:
            print(result)

        print(results.hits.total, 'hits total')
        for hit in results:
            print(hit.meta.score, hit.name)

        for (code, count, selected) in results.facets.code:
            print(code, ' (SELECTED):' if selected else ':', count)
