# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('background_type', models.CharField(max_length=64, choices=[('light', 'Light'), ('dark', 'Dark')])),
                ('caption_position', models.CharField(max_length=64, choices=[('center', 'Center'), ('left', 'Left'), ('right', 'right')])),
                ('title', models.CharField(max_length=64)),
                ('title_type', models.CharField(max_length=64, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')])),
                ('title2', models.CharField(max_length=64)),
                ('title_type2', models.CharField(max_length=64, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')])),
                ('title3', models.CharField(max_length=64)),
                ('title_type3', models.CharField(max_length=64, choices=[('slide-caption-title', 'Caption Title'), ('slide-caption-title-uppercase', 'Caption Title Uppercase'), ('subtitle-top-uppercase', 'Subtitle Top Uppercase'), ('subtitle-bottom-uppercase', 'Subtitle Bottom Uppercase'), ('subtitle-title-sale-uppercase', 'Title Sale Uppercase')])),
                ('link', models.URLField()),
                ('link_title', models.CharField(max_length=64)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='slider')),
            ],
        ),
    ]
