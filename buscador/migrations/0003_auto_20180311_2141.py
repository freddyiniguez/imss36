# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0002_auto_20180311_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='especialidad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_cita',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cita',
            name='lugar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cita',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]