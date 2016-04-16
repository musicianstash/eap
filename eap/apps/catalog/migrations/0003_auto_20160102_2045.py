# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160102_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ColorOption',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('attribute', models.ForeignKey(null=True, to='catalog.Color')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.ForeignKey(null=True, to='catalog.Color'),
        ),
    ]
