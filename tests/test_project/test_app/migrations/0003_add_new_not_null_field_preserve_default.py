# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_add_new_not_null_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='a',
            name='new_not_null_field_preserve_default',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
