# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link_title',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title2',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title3',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title_type',
            field=models.CharField(choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title_type2',
            field=models.CharField(choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title_type3',
            field=models.CharField(choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64, blank=True),
        ),
    ]
