# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_categorykey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorykey',
            name='category',
        ),
        migrations.DeleteModel(
            name='CategoryKey',
        ),
    ]
