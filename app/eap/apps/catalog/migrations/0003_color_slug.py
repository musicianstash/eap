# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160507_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(default='test', max_length=64),
            preserve_default=False,
        ),
    ]