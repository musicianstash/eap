# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0003_brandkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='featured',
            new_name='is_popular',
        ),
    ]
