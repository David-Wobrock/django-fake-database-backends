# Generated by Django 2.0.1 on 2018-02-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0032_drop_field_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondobject',
            name='filepath',
            field=models.FilePathField(null=True, unique=True),
        ),
    ]