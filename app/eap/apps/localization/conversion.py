# -*- coding: utf-8 -*-
from collections import namedtuple
from operator import itemgetter
from decimal import Decimal
from datetime import timedelta

from django.conf import settings

from .adapters import BaseAdapter
from .cache import (update_rates_cached, get_rate_cached, get_rates_cached,
                    CACHE_ENABLED, set_cached_rate)
from .models import ExchangeRate
from .utils import import_class, memoize
from .adapters.openexchangerates import OpenExchangeRatesAdapter


Price = namedtuple('Price', ('value', 'currency'))

EXCHANGE_ADAPTER_CLASS_KEY = 'EXCHANGE_ADAPTER_CLASS'
EXCHANGE_DEFAULT_ADAPTER_CLASS = 'eap.apps.localization.adapters.openexchangerates.OpenExchangeRatesAdapter'


def update_rates(adapter_class_name=None):
    adapter_class_name = (adapter_class_name or
                          getattr(settings,
                                  EXCHANGE_ADAPTER_CLASS_KEY,
                                  EXCHANGE_DEFAULT_ADAPTER_CLASS))

    adapter_class = OpenExchangeRatesAdapter
    adapter = adapter_class()
    if not isinstance(adapter, BaseAdapter):
        raise TypeError("invalid adapter class: {}".format(adapter_class_name))
    adapter.update()

    if CACHE_ENABLED:
        update_rates_cached()


def convert_values(args_list):
    """convert_value in bulk.

    :param args_list: list of value, source, target currency pairs

    :return: map of converted values
    """
    rate_map = get_rates(map(itemgetter(1, 2), args_list))
    value_map = {}
    for value, source, target in args_list:
        args = (value, source, target)
        value_map[args] = value if source == target else value * rate_map[(source, target)]
    return value_map


def get_rates(currencies):
    sources = []
    targets = []

    if CACHE_ENABLED:
        rate_map = get_rates_cached(currencies)
        for (source, target), rate in rate_map.items():
            if not rate:
                sources.append(source)
                targets.append(target)
    else:
        rate_map = {c: None for c in currencies}
        sources = map(itemgetter(0), currencies)
        targets = map(itemgetter(1), currencies)

    rates = ExchangeRate.objects.filter(
        source__code__in=sources,
        target__code__in=targets).values_list(
        'source__code',
        'target__code',
        'rate')

    for source, target, rate in rates:
        key = (source, target)
        # Some other combinations that are not in currencies originally
        # may have been fetched from the query
        if key in rate_map:
            rate_map[key] = rate

    return rate_map


@memoize(ttl=timedelta(hours=1))
def get_rate(source_currency, target_currency):
    rate = None

    if CACHE_ENABLED:
        rate = get_rate_cached(source_currency, target_currency)

    if not rate:
        rate = ExchangeRate.objects.get_rate(source_currency, target_currency)

        if CACHE_ENABLED:
            set_cached_rate(source_currency, target_currency, rate)

    return rate


def convert_value(value, source_currency, target_currency):
    """Converts the price of a currency to another one using exchange rates

    :param price: the price value
    :param type: decimal

    :param source_currency: source ISO-4217 currency code
    :param type: str

    :param target_currency: target ISO-4217 currency code
    :param type: str

    :returns: converted price instance
    :rtype: ``Price``

    """
    # If price currency and target currency is same return given currency as is
    if source_currency == target_currency:
        return value_to_decimal(value)

    rate = get_rate(source_currency, target_currency)

    return value_to_decimal(value) * rate


def value_to_decimal(value):
    """Helper method to convert any price value type into Decimal type.

    :param value: the price value
    :param type: mixed

    :returns: converted value instance to Decimal type
    :rtype: ``Decimal``

    """
    if isinstance(value, (str, float)):

        if isinstance(value, float):
            value = str(value)

        return Decimal(value)
    return value


def convert(price, currency):
    """Shorthand function converts a price object instance of a source
    currency to target currency

    :param price: the price value
    :param type: decimal

    :param currency: target ISO-4217 currency code
    :param type: str

    :returns: converted price instance
    :rtype: ``Price``

    """
    # If price currency and target currency is same return given currency as is
    value = convert_value(price.value, price.currency, currency)
    return Price(value, currency)
