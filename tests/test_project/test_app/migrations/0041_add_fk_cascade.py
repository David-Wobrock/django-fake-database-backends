# Generated by Django 2.0.1 on 2018-02-04 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0040_drop_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstobject',
            name='obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.SecondObject'),
        ),
    ]
