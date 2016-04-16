# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import mptt.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('value', models.CharField(max_length=32)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField()),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField()),
                ('name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='categories')),
                ('order', models.IntegerField(default=0)),
                ('meta_keywords', models.TextField(blank=True, max_length=255)),
                ('meta_description', models.TextField(blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryAttributeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('attribute_group', models.ForeignKey(to='catalog.AttributeGroup')),
                ('category', models.ForeignKey(to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type', models.SmallIntegerField(choices=[(1, 'Normal type'), (2, 'Spider type')], default=1)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published'), (3, 'Disabled'), (4, 'Ignored')], default=1)),
                ('spider_code', models.CharField(blank=True, max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('affiliate_url', models.URLField(blank=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('sale_price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('attribute', smart_selects.db_fields.ChainedForeignKey(chained_field='attribute_group', to='catalog.Attribute', chained_model_field='attribute_group')),
                ('attribute_group', models.ForeignKey(to='catalog.AttributeGroup')),
                ('item', models.ForeignKey(to='catalog.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='products')),
                ('hash_tag', models.CharField(blank=True, max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(related_name='images', to='catalog.Item')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='attributes',
            field=models.ManyToManyField(to='catalog.Attribute', through='catalog.ItemAttribute'),
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(to='brand.Brand'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, to='catalog.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='attribute_groups',
            field=models.ManyToManyField(to='catalog.AttributeGroup', through='catalog.CategoryAttributeGroup'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, related_name='children', to='catalog.Category'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_group',
            field=models.ForeignKey(null=True, to='catalog.AttributeGroup'),
        ),
    ]
