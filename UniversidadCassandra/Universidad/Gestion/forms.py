from django import forms
from django.db import models

from .models import carrera


class AulasForm(forms.Form):
    nro       = forms.IntegerField(label='Número de Aula')
    piso      = forms.CharField(label='Piso', max_length=2)
    capacidad = forms.IntegerField(label='Capacidad de Alumnos')


class MateriasForm(forms.Form):
    nombre  = forms.CharField(label='Nombre', max_length=50)
    carrera = forms.CharField(label='Carrera', max_length=100)
    #carrera = forms.OneToOneField (carrera, null=False, blank=False, on_delete=models.CASCADE)