# Generated by Django 2.0.1 on 2018-01-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0027_add_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondobject',
            name='floating_second',
            field=models.FloatField(default=5.673),
        ),
    ]
