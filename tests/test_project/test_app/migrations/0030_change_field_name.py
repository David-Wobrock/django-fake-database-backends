# Generated by Django 2.0.1 on 2018-02-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0029_add_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondobject',
            name='mail',
            field=models.EmailField(db_column='email_address', default='test@example.com', max_length=254),
        ),
    ]
