# Generated by Django 2.0.1 on 2018-01-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_create_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
            ],
        ),
    ]
