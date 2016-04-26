# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('background_type', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], max_length=64)),
                ('caption_position', models.CharField(choices=[('center', 'Center'), ('left', 'Left'), ('right', 'right')], max_length=64)),
                ('title', models.CharField(blank=True, max_length=64)),
                ('title_type', models.CharField(blank=True, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64)),
                ('title2', models.CharField(blank=True, max_length=64)),
                ('title_type2', models.CharField(blank=True, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64)),
                ('title3', models.CharField(blank=True, max_length=64)),
                ('title_type3', models.CharField(blank=True, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')], max_length=64)),
                ('link', models.URLField(blank=True)),
                ('link_title', models.CharField(blank=True, max_length=64)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='slider')),
            ],
        ),
    ]
