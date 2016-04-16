# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160102_1046'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(default=1, to='store.Store'),
            preserve_default=False,
        ),
    ]
