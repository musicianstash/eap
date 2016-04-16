# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_auto_20160102_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandKey',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('brand', models.ForeignKey(to='brand.Brand', null=True)),
            ],
        ),
    ]
