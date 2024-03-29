# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Running'), (2, 'Queue'), (3, 'Running'), (4, 'Stopping')], default=1)),
                ('name', models.CharField(max_length=64)),
                ('download_delay', models.FloatField(default=0)),
                ('concurrent_requests', models.FloatField(default=8)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]
