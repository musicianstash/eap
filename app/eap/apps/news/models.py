# -*- coding: utf-8 -*-
from eap.extensions.mailchimp.utils import get_mailchimp_api

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from mailchimp3.helpers import get_subscriber_hash

# State of Article
DRAFT = 0
HIDDEN = 1
PUBLISHED = 2

STATUS_CHOICES = (
    (DRAFT, 'draft'),
    (HIDDEN, 'hidden'),
    (PUBLISHED, 'published'),
)


class ArticleCategory(models.Model):
    """Model holds category for articles"""
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        get_latest_by = 'order'
        ordering = ['order']

    def __str__(self):
        return self.name


class Article(models.Model):
    """Model holds news article"""
    category = models.ForeignKey(ArticleCategory, related_name='category', on_delete=models.PROTECT)
    content = models.TextField()
    excerpt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(User, related_name='publisher')
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    slug = models.SlugField(max_length=64)

    # sortable property
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        get_latest_by = 'published_at'
        ordering = ['-published_at']

    def has_images(self):
        """Check if article contains images"""
        return self.images.exists()

    def first_image(self):
        """Retrieve first image url defined for that article"""
        images = self.images.all()
        return images[0] if images else None

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    """Model holds images for news article"""
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles')


class Subscriber(models.Model):
    """Model holds subscription to newsletter."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True)
    subscribed = models.BooleanField(default=True)
    latest_news = models.BooleanField(default=True)
    new_product = models.BooleanField(default=True)
    offer = models.BooleanField(default=True)

    @property
    def member_id(self):
        return get_subscriber_hash(self.email.encode('utf-8'))

    def save(self, *args, **kwargs):
        # we can have users on newsletter that are not registered on site
        if self.user:
            self.email = self.user.email
        self.update_mailchimp()
        super(Subscriber, self).save(*args, **kwargs)

    def sync_from_mailchimp(self):
        # TODO: trigger this via webhooks
        """Sync our model with state on MailChimp side."""
        api = get_mailchimp_api()

        # get member from list and his status
        member = api.member.get(settings.MAILCHIMP_LIST_NEWSLETTER_ID, self.member_id)

        # for non existent members, status contains 404 code
        if member['status'] != 404:
            self.subscribed = self.status_to_subscribed(member['status'])
            self.latest_news = member['interests'][settings.MAILCHIMP_LATEST_NEWS_ID]
            self.new_product = member['interests'][settings.MAILCHIMP_NEW_PRODUCT_ID]
            self.offer = member['interests'][settings.MAILCHIMP_OFFER_ID]
            self.save()

    def update_mailchimp(self):
        """Update list on MailChimp side."""
        api = get_mailchimp_api()

        data = {'email_address': self.email, 'status': self.__unicode__().lower(), 'interests': {
            settings.MAILCHIMP_LATEST_NEWS_ID: self.latest_news,
            settings.MAILCHIMP_NEW_PRODUCT_ID: self.new_product,
            settings.MAILCHIMP_OFFER_ID: self.offer}
        }

        if self.user:
            # TODO: add other data, such as name, surname, etc.
            pass
        api.member.create_or_update(settings.MAILCHIMP_LIST_NEWSLETTER_ID, self.member_id, data=data)

    @staticmethod
    def status_to_subscribed(status):
        return True if status == 'subscribed' else False

    def __unicode__(self):
        if self.subscribed:
            return 'Subscribed'
        else:
            return 'Unsubscribed'

    def __str__(self):
        return self.email
