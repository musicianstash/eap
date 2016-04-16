# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
