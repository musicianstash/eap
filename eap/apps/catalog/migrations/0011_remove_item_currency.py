# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_item_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='currency',
        ),
    ]
