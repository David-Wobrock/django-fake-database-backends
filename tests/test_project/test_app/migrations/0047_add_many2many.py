# Generated by Django 2.0.1 on 2018-02-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0046_add_one2one'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondobject',
            name='many2many',
            field=models.ManyToManyField(to='test_app.FirstObject'),
        ),
    ]