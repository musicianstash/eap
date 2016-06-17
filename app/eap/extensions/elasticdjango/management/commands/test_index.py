from django.core.management.base import BaseCommand

from eap.apps.catalog.documents import ItemDoc, ItemSearch


class Command(BaseCommand):
    es = None

    def handle(self, *args, **kwargs):
        bs = ItemSearch(None, {
            # 'brands': ['l'],
            'category_ids': [5]
        })

        bs = bs[0:20]

        results = bs.execute()

        # access hits and other attributes as usual
        print(results.hits.total, 'hits total')

        print("=================================")
        print("CATEGORIES")
        for (color, count, selected) in results.facets['category_ids']:
            print(color, ' (SELECTED):' if selected else ':', count)

        print("==========================")

        for result in results:
            print(result['name'] + " : " + result['brand'] + " : " + str(result['rounded_discount']))


        # results = ItemDoc().search().execute()
        #
        # for result in results:
        #     print(result['brand'])

        # print(results.hits.total, 'hits total')
        # for hit in results:
        #     print(hit.meta.score, hit.name)
        #
        # for (code, count, selected) in results.facets.code:
        #     print(code, ' (SELECTED):' if selected else ':', count)
