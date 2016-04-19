# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """Model holds news article"""
    content = models.TextField()
    category = models.ForeignKey('categories.Category')
    published_date = models.DateField()
    created_date = models.DateField()
    updated_date = models.DateField()
    title = models.CharField(max_length=255)
    reporter = models.ForeignKey(User, related_name='reporter')

    # sortable property
    order = models.PositiveIntegerField()



class ArticleImage(models.Model):
    """Model holds images for news article"""
    article = models.ForeignKey(Article, related_name='images')
    image = models.ImageField(upload_to='articles')


