# Generated by Django 2.0.1 on 2018-02-04 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0038_rename_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherobject',
            old_name='other_id',
            new_name='renamed_id',
        ),
    ]