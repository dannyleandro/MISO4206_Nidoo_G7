# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181006_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='cliente',
            new_name='Cliente',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='fecha',
            new_name='Fecha',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='parqueadero',
            new_name='Parqueadero',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='vehiculo',
            new_name='Vehiculo',
        ),
    ]
