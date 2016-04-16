# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_category_is_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
