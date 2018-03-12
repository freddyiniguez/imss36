# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# - - - C I T A - - - #
# Contiene informacion de la cita medica
class Cita(models.Model):
	fecha_relacion = models.DateField()
	fecha_recibo = models.IntegerField()
	nombre = models.CharField(max_length = 100)
	nss = models.CharField(max_length = 50)
	dx = models.CharField(max_length = 60)
	lugar = models.CharField(max_length = 100, blank=True)
	especialidad = models.CharField(max_length = 100, blank=True)
	fecha_cita = models.CharField(max_length = 100, blank=True)
	status = models.CharField(max_length = 50, blank=True)

	def __str__(self):
		return self.nombre