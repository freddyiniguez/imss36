# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportMixin
from import_export import resources, fields
from .models import Cita

class CitaResource(resources.ModelResource):
	fecha_relacion = fields.Field(
		attribute = 'fecha_relacion',
		column_name = 'FECHA DE RELACIÓN'
	)

	fecha_recibo = fields.Field(
		attribute = 'fecha_recibo',
		column_name = 'FECHA DE RECIBIDO'
	)

	nombre = fields.Field(
		attribute = 'nombre',
		column_name = 'NOMBRE DEL PACIENTE'
	)

	nss = fields.Field(
		attribute = 'nss',
		column_name = 'No. DE AFILIACION'
	)

	dx = fields.Field(
		attribute = 'dx',
		column_name = 'DIAGNOSTICO'
	)

	lugar = fields.Field(
		attribute = 'lugar',
		column_name = 'LUGAR'
	)

	especialidad = fields.Field(
		attribute = 'especialidad',
		column_name = 'ESPECIALIDAD'
	)

	fecha_cita = fields.Field(
		attribute = 'fecha_cita',
		column_name = 'FECHA DE CITA'
	)

	def get_instance(self, instance_loader, row):
		return False

	class Meta:
		model = Cita
		fields = ('fecha_relacion', 'fecha_recibo', 'nombre', 'nss', 'dx', 'lugar', 'especialidad', 'fecha_cita')
		export_order = fields

class CitaAdmin(ImportMixin, admin.ModelAdmin):
	resource_class = CitaResource

admin.site.register(Cita, CitaAdmin)
