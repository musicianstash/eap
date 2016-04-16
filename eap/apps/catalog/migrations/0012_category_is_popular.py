# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_item_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_popular',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
