# Generated by Django 2.0.1 on 2018-01-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_create_table_with_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstobject',
            name='name',
            field=models.CharField(default='empty', max_length=30),
        ),
    ]
