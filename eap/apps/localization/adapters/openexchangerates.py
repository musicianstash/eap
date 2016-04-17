# -*- coding: utf-8 -*-
import logging

from django.conf import settings

from ..adapters import BaseAdapter
from ..utils.openexchangerates import OpenExchangeRatesClient

logger = logging.getLogger(__name__)


class OpenExchangeRatesAdapter(BaseAdapter):
    """This adapter uses openexchangerates.org service to populate currency and
    exchange rate models.
    """

    API_KEY_SETTINGS_KEY = 'OPENEXCHANGERATES_API_KEY'

    def __init__(self):
        self.client = OpenExchangeRatesClient(getattr(settings, self.API_KEY_SETTINGS_KEY))

    def get_currencies(self):
        return self.client.currencies().items()

    def get_exchangerates(self, base):
        return self.client.latest(base)['rates'].items()
