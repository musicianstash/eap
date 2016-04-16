# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20160102_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coloroption',
            old_name='attribute',
            new_name='color',
        ),
    ]
