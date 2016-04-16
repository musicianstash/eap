# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '__first__'),
        ('catalog', '0008_category_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(default=1, to='localization.Currency'),
            preserve_default=False,
        ),
    ]
