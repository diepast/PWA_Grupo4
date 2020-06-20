from django.db import models

# Create your models here.


class aula(models.Model):
    nroAula = models.CharField(max_length=2, primary_key=True)
    piso = models.CharField(max_length=2)
    capacidad = models.IntegerField()

    def __str__(self):
        return 'Nro Aula:' "{0} Piso:{1} => Capacidad: {2}".format(self.nroAula, self.piso, self.capacidad)
