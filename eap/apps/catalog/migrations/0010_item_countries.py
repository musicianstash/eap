# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_item_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='countries',
            field=models.TextField(blank=True),
        ),
    ]
