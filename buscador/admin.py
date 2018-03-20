# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportMixin
from import_export import resources, fields
from .models import Cita

class CitaResource(resources.ModelResource):
	nombre = fields.Field(
		attribute = 'nombre',
		column_name = 'NOMBRE DEL PACIENTE'
	)

	nss = fields.Field(
		attribute = 'nss',
		column_name = 'No. DE AFILIACION'
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

	status = fields.Field(
		attribute = 'status',
		column_name = 'ESTATUS'
	)

	def get_instance(self, instance_loader, row):
		return False

	class Meta:
		model = Cita
		fields = ('nombre', 'nss', 'lugar', 'especialidad', 'fecha_cita', 'status')
		export_order = fields

class CitaAdmin(ImportMixin, admin.ModelAdmin):
	resource_class = CitaResource

admin.site.register(Cita, CitaAdmin)
