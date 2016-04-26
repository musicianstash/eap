# -*- coding: utf-8 -*-
from django.db import models

from .managers import ExchangeRateManager


class Currency(models.Model):
    """Model holds a currency information for a nationality"""
    code = models.CharField(max_length=3, unique=True)
    prefix = models.CharField(max_length=10)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    """Model to persist exchange rates between currencies"""
    source = models.ForeignKey(Currency, related_name='rates')
    target = models.ForeignKey(Currency)
    rate = models.DecimalField(max_digits=17, decimal_places=8)

    objects = ExchangeRateManager()

    def __str__(self):
        return '{} / {} = {}'.format(self.source, self.target, self.rate)


class Country(models.Model):
    is_active = models.BooleanField(default=False)

    # Description fields
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=2)
    currency = models.ForeignKey(Currency)

    def __str__(self):
        return self.name
