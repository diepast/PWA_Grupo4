from django.urls import path

from . import views

app_name = 'Gestion'
urlpatterns = [
	# ex: /gestion/
    path('', views.index, name='index'),
	# ex: /gestion/aulas
	path('aulas/', views.aulas, name='aulas'),
	# ex: /gestion/aulas/listado
	path('aulas/listado/', views.ListarAulas, name='lista_aulas'),
    # ex: /gestion/materias
	path('materias/', views.materias, name='materias'),
]