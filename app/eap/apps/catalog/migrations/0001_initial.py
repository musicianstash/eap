# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('is_popular', models.BooleanField()),
                ('name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='categories')),
                ('meta_keywords', models.TextField(blank=True, max_length=255)),
                ('meta_description', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ColorKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('order', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Color')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(1, 'Normal type'), (2, 'Spider type')], default=1)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published'), (3, 'Disabled'), (4, 'Ignored')], default=1)),
                ('spider_code', models.CharField(blank=True, max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('affiliate_url', models.URLField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('countries', models.TextField(blank=True)),
                ('in_stock', models.BooleanField(default=False)),
                ('meta_keywords', models.TextField(blank=True, max_length=255)),
                ('meta_description', models.TextField(blank=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.Brand')),
                ('category', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Color')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='products')),
                ('hash_tag', models.CharField(blank=True, max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.Item')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='PriceAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('email', models.EmailField(max_length=254)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_alert', to='catalog.Item')),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
        ),
        migrations.CreateModel(
            name='StockAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_alert', to='catalog.Item')),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
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