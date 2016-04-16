from django.db import models


class ExchangeRateManager(models.Manager):

    def get_queryset(self):
        queryset = super(ExchangeRateManager, self).get_queryset()
        return queryset.select_related('source', 'target')

    def get_rate(self, source_currency, target_currency):
        return self.get(source__code=source_currency,
                        target__code=target_currency).rate
