# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_relacion', models.DateField()),
                ('fecha_recibo', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('nss', models.CharField(max_length=50)),
                ('dx', models.CharField(max_length=60)),
                ('lugar', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('fecha_cita', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=5)),
            ],
        ),
    ]
