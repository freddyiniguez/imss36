# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-14 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0003_auto_20180311_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha_recibo',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_relacion',
            field=models.DateTimeField(),
        ),
    ]
