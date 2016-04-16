# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField()),
                ('name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='stores')),
                ('meta_keywords', models.TextField(blank=True, max_length=255)),
                ('meta_description', models.TextField(blank=True)),
            ],
        ),
    ]
