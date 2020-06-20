from django.db import models
from apps.materia.models import materia

# Create your models here.


class cursada(models.Model):
    idCursada = models.CharField(max_length=2, primary_key=True)
    materia = models.ForeignKey(
        materia, null=False, blank=False, on_delete=models.CASCADE)
    cantidadAlumnos = models.IntegerField()

    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.idCursada, self.materia, self.cantidadAlumnos)
