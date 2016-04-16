# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20160117_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
