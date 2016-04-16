# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20160117_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='attribute_group',
        ),
        migrations.RemoveField(
            model_name='categoryattributegroup',
            name='attribute_group',
        ),
        migrations.RemoveField(
            model_name='categoryattributegroup',
            name='category',
        ),
        migrations.RemoveField(
            model_name='itemattribute',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='itemattribute',
            name='attribute_group',
        ),
        migrations.RemoveField(
            model_name='itemattribute',
            name='item',
        ),
        migrations.RemoveField(
            model_name='category',
            name='attribute_groups',
        ),
        migrations.RemoveField(
            model_name='item',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.DeleteModel(
            name='AttributeGroup',
        ),
        migrations.DeleteModel(
            name='CategoryAttributeGroup',
        ),
        migrations.DeleteModel(
            name='ItemAttribute',
        ),
    ]
