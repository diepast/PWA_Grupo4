from django.db import models
from apps.comision.models import comisionN
from apps.aula.models import aula
from apps.cursada.models import cursada
from apps.materia.models import materia

# Create your models here.


class cursadaAula(models.Model):
    idCursada = models.OneToOneField(
        cursada, null=False, blank=False, on_delete=models.CASCADE)
    nroAula = models.OneToOneField(
        aula, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.idCursada, self.nroAula)


class comisionMateria(models.Model):
    NombredeMateria = models.OneToOneField(
        materia, null=False, blank=False, on_delete=models.CASCADE)
    comision = models.ForeignKey(
        comisionN, blank=False, default=None, on_delete=models.CASCADE)
    dias = (('Lun', 'Lunes'), ('Mar', 'Martes'), ('Mie', 'Miércoles'),
            ('Jue', 'Jueves'), ('Vie', 'Viernes'))
    dia = models.CharField(max_length=3, choices=dias, default='Lun')

    def __str__(self):
        cadena = "{0} {1}=> {2}"
        return cadena.format(self.NombredeMateria, self.comision, self.dia)
