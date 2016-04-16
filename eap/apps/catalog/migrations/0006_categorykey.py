# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160105_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryKey',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('category', models.ForeignKey(null=True, to='catalog.Color')),
            ],
        ),
    ]
