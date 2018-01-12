# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_remove_a_new_not_null_field_preserve_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='a',
            name='mybiginteger',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='mybinary',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myboolean',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='a',
            name='mychar',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='mydecimal',
            field=models.DecimalField(decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myduration',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myemail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myfile',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='a',
            name='myfilepath',
            field=models.FilePathField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myfloat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='mygenericipaddress',
            field=models.GenericIPAddressField(default='8.8.8.8'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a',
            name='myimage',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='a',
            name='mynullboolean',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='a',
            name='mypositiveinteger',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='a',
            name='mypositivesmallinteger',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myslug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='mytext',
            field=models.TextField(default='Test text', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a',
            name='myurl',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='a',
            name='myuuid',
            field=models.UUIDField(null=True, unique=True),
        ),
    ]
