# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Cita


# - - - H O M E - - - #
# Pantalla de inicio
def home(request):
	citas_list = Cita.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(citas_list, 5)
	try:
		citas = paginator.page(page)
	except PageNotAnInteger:
		citas = paginator.page(1)
	except EmptyPage:
		citas = paginator.page(paginator.num_pages)
	return render(request, 'buscador/index.html', {'citas': citas, 'mensaje': ''})


# - - - B U S C A D O R - - - #
# Funcionalidad para buscar la cita de un paciente
def buscador(request):
	 query = request.GET.get('name')

	 if query=="":
	 	return render(request, 'buscador/index.html', {'mensaje': 'INGRESE UN NOMBRE PARA BUSCAR'})
	 
	 citas_list = Cita.objects.all().filter(nombre__icontains=query).values()

	 if not citas_list:
	 	return render(request, 'buscador/buscador.html', {'citas':'0 resultados', 'mensaje': 'NO SE ENCONTRARON RESULTADOS'})
	 else:
	 	return render(request, 'buscador/buscador.html', {'citas': citas_list, 'mensaje':' '})


# - - - I M P O R T A R - - - #
# Funcionalidad para importar un archivo de excel y guardar la informacion en la BD
@login_required
def importar(request):
	return render(request, 'buscador/importar.html', {})