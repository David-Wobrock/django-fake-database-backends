# Generated by Django 2.0.1 on 2018-01-21 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_add_not_null_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondobject',
            name='code',
        ),
    ]
