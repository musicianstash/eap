# -*- coding: utf-8 -*-
from mailchimp3 import MailChimp
from django.conf import settings


def get_mailchimp_api():
    """Creates client instance to access MailChimp API. """
    return MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_SECRET_API_KEY)