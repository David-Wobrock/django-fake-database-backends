# Generated by Django 2.0.1 on 2018-02-04 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0042_remove_fk_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstobject',
            name='fk_protect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='test_app.FirstObject'),
        ),
    ]
