# Generated by Django 2.0.1 on 2018-02-04 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0041_add_fk_cascade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstobject',
            name='obj',
            field=models.ForeignKey(db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.SecondObject'),
        ),
    ]
