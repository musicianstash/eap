# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20160122_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceAlert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
            name='StockAlert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='catalog.Item', related_name='stock_alert')),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='itempricealert',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='itempricealert',
            name='item',
        ),
        migrations.AlterUniqueTogether(
            name='itemstockalert',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='itemstockalert',
            name='item',
        ),
        migrations.DeleteModel(
            name='ItemPriceAlert',
        ),
        migrations.DeleteModel(
            name='ItemStockAlert',
        ),
        migrations.AlterUniqueTogether(
            name='stockalert',
            unique_together=set([('item', 'email')]),
        ),
        migrations.AlterUniqueTogether(
            name='pricealert',
            unique_together=set([('item', 'email')]),
        ),
    ]
