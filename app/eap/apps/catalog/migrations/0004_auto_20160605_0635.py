# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 06:35
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_color_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='spider_code',
            new_name='code',
        ),
        migrations.AddField(
            model_name='item',
            name='related_colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=[], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='skus',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=[], size=None),
            preserve_default=False,
        ),
    ]