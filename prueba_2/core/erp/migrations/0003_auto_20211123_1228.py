# Generated by Django 3.0.8 on 2021-11-23 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auxiliar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auxiliar',
            old_name='cuento',
            new_name='relatoUsuario',
        ),
    ]
