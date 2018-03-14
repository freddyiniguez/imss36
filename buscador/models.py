# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# - - - C I T A - - - #
# Contiene informacion de la cita medica
class Cita(models.Model):
	fecha_relacion = models.DateTimeField()
	fecha_recibo = models.DateTimeField()
	nombre = models.CharField(max_length = 100)
	nss = models.CharField(max_length = 50)
	dx = models.CharField(max_length = 200)
	lugar = models.CharField(max_length = 200, blank=True)
	especialidad = models.CharField(max_length = 200, blank=True)
	fecha_cita = models.TextField(blank=True)
	status = models.CharField(max_length = 250, blank=True)

	def __str__(self):
		return self.nombre