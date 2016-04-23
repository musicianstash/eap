# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

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
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(User, related_name='publisher')
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    # sortable property
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        get_latest_by = 'published_at'
        ordering = ['-published_at']

    def __str__(self):
        return self.title



class ArticleImage(models.Model):
    """Model holds images for news article"""
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles')


