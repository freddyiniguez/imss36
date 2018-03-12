# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cita


# - - - H O M E - - - #
# Pantalla de inicio
def home(request):
	return render(request, 'buscador/index.html', {})


# - - - B U S C A D O R - - - #
# Funcionalidad para buscar la cita de un paciente
def buscador(request):
	 query = request.GET.get('name')
	 result = Cita.objects.all().filter(nombre__icontains=query)

	 if not result:
	 	return render(request, 'buscador/importar.html', {'result':'0 resultados', 'mensaje': 'NO SE ENCONTRARON RESULTADOS'})
	 else:
	 	return render(request, 'buscador/buscador.html', {'result': result, 'mensaje':' '})


# - - - I M P O R T A R - - - #
# Funcionalidad para importar un archivo de excel y guardar la informacion en la BD
@login_required
def importar(request):
	return render(request, 'buscador/importar.html', {})