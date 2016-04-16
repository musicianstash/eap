# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20160117_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colorkey',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='colorkey',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
