# Generated by Django 2.0.1 on 2018-02-04 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0043_add_fk_protect'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstobject',
            name='fk_set_null',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theotherfield', to='test_app.SecondObject'),
        ),
    ]
