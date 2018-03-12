from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^importar/$', views.importar, name = 'importar'),
	url(r'^buscador/$', views.buscador, name = 'buscador'),
]