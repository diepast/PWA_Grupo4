from django.urls import path

from . import views

app_name = 'Reportes'
urlpatterns = [
	# ex: /reportes/
    path('', views.index, name='index'),
]