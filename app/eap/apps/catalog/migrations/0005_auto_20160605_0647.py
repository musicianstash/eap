# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 06:47
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20160605_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='skus',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, size=None),
        ),
    ]
