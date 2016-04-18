# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """Model holds news article"""
    pub_date = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    reporter = models.ForeignKey(User)

    # TODO: define methods
    # TODO: Check this implementation: https://github.com/Fantomas42/django-blog-zinnia/blob/develop/zinnia/models_bases/entry.py

