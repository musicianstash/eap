# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail import ImageField


class Slider(models.Model):
    BACKGROUND_TYPE_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark')
    )

    TITLE_TYPE_CHOICES = (
        ('slide-caption-title', 'Caption Title'),
        ('slide-caption-title-uppercase', 'Caption Title Uppercase'),
        ('subtitle-top-uppercase', 'Subtitle Top Uppercase'),
        ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'),
        ('subtitle-title-sale-uppercase', 'Title Sale Uppercase'),
    )

    CAPTION_POSITION_CHOICES = (
        ('center', 'Center'),
        ('left', 'Left'),
        ('right', 'right'),
    )

    is_active = models.BooleanField(default=False)
    background_type = models.CharField(max_length=64, choices=BACKGROUND_TYPE_CHOICES)
    caption_position = models.CharField(max_length=64, choices=CAPTION_POSITION_CHOICES)

    # Description fields
    title = models.CharField(max_length=64, blank=True)
    title_type = models.CharField(max_length=64, choices=TITLE_TYPE_CHOICES, blank=True)

    title2 = models.CharField(max_length=64, blank=True)
    title_type2 = models.CharField(max_length=64, choices=TITLE_TYPE_CHOICES, blank=True)

    title3 = models.CharField(max_length=64, blank=True)
    title_type3 = models.CharField(max_length=64, choices=TITLE_TYPE_CHOICES, blank=True)

    link = models.URLField(blank=True)
    link_title = models.CharField(max_length=64, blank=True)

    # Image field
    image = ImageField(upload_to='slider', blank=True)

    def __str__(self):
        return self.title
