from django.db import models

# Create your models here.


class materia(models.Model):
    idMateria = models.CharField(max_length=2, primary_key=True)
    NombredeMateria = models.CharField(max_length=45)
    Carrera = models.CharField(max_length=45)

    def MateriasPorCarrera(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.idMateria, self.NombredeMateria, self.Carrera)

    def __str__(self):
        return self.MateriasPorCarrera()
