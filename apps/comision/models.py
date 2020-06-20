from django.db import models
from apps.aula.models import aula

# Create your models here.


class turnoN(models.Model):
    turnos = (('T', 'Tarde: 13:00 a 19:00'), ('N', 'Noche: 19:00 a 23:00'))
    turno = models.CharField(
        max_length=1, choices=turnos, default='N')
    NroAula = models.OneToOneField(
        aula, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return 'Turno:' "{0} Aula:{1}".format(self.NroAula, self.turno)


class comisionN(models.Model):
    comisiones = (('1A', 'Comision_1A'), ('1B', 'Comision_1B'), ('2A', 'Comision_2A'), ('2B', 'Comision_2B'),
                  ('3A', 'Comision_3A'), ('3B', 'Comision_3B'), ('4A', 'Comision_4A'), ('4B', 'Comision_4B'))
    comision = models.CharField(
        max_length=2, choices=comisiones, default='1A')
    turno = models.ForeignKey(
        turnoN, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comisión:' "{0} Turno:{1}".format(self.comision, self.turno)
