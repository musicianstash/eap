# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160105_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.TextField(blank=True),
        ),
    ]
