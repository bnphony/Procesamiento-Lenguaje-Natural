# Generated by Django 3.0.8 on 2021-12-08 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20211207_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='accion',
            name='aux',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.Auxiliar', verbose_name='Auxiliar'),
            preserve_default=False,
        ),
    ]
