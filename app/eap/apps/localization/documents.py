# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType, field
from elasticsearch_dsl import FacetedSearch, TermsFacet, DateHistogramFacet

from .models import Currency


class CurrencyDoc(DocType):
    code = field.String()
    prefix = field.String()
    name = field.String()

    class Meta:
        index = 'dps'
        doc_type = 'currency'

    @classmethod
    def sync_index(cls):
        for model in Currency.objects.all().iterator():
            cls.sync(model)

    @classmethod
    def sync(cls, model_obj):
        album_doc = CurrencyDoc(meta={'id': model_obj.id})
        album_doc.name = model_obj.name
        album_doc.code = model_obj.code
        album_doc.prefix = model_obj.prefix
        album_doc.save()

    def get_model_obj(self):
        return Currency.objects.get(id=self.meta.id)


CurrencyDoc.init()


class CurrencySearch(FacetedSearch):
    doc_types = [CurrencyDoc, ]
    # fields that should be searched
    fields = ['name', 'code', 'prefix']

    facets = {
        # use bucket aggregations to define facets
        'code': TermsFacet(field='code')
    }
