# Generated by Django 2.0.1 on 2018-02-04 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0044_add_fk_set_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstobject',
            name='fk_do_nothing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='donothing', to='test_app.SecondObject'),
        ),
    ]