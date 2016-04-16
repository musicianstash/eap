# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20160117_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPriceAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('email', models.EmailField(max_length=254)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='catalog.Item', related_name='price_alert')),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
        ),
        migrations.CreateModel(
            name='ItemStockAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='catalog.Item', related_name='stock_alert')),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='itemstockalert',
            unique_together=set([('item', 'email')]),
        ),
        migrations.AlterUniqueTogether(
            name='itempricealert',
            unique_together=set([('item', 'email')]),
        ),
    ]
