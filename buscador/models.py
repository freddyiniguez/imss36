# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# - - - C I T A - - - #
# Contiene informacion de la cita medica

@python_2_unicode_compatible
class Cita(models.Model):
	nombre = models.TextField(blank=True, null=True)
	nss = models.TextField(blank=True, null=True)
	lugar = models.TextField(blank=True, null=True)
	especialidad = models.TextField(blank=True, null=True)
	fecha_cita = models.TextField(blank=True, null=True)
	status = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.nombre