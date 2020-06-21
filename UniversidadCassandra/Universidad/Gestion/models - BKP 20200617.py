from django.db import models

# Create your models here.


class Cursadas(models.Model):
    NombredeMateria = models.CharField(max_length=45)
    Carrera = models.CharField(max_length=45)
    CantidadAlumnos = models.IntegerField()
    Comisiones = (('A', 'Comision A'), ('B', 'Comision B'))
    Comision = models.CharField(max_length=1, choices=Comisiones, default='A')
    Turnos = (('T', 'Tarde'), ('N', 'Noche'))
    Turno = models.CharField(max_length=1, choices=Turnos, default='N')

    def AlumnosPorMateria(self):
        cadena = "{0} {1} {2} {3}, {4}"
        return cadena.format(self.Carrera, self.NombredeMateria, self.Turno, self.Comision, self.CantidadAlumnos)

    def __str__(self):
        return self.AlumnosPorMateria()


class Aulas(models.Model):
    NroAula = models.CharField(max_length=2)
    Piso = models.CharField(max_length=2)
    Capacidad = models.IntegerField()

    def CapacidadAulas(self):
        cadena = "Nro Aula:{0} Piso:{1}-> Capacidad:{2}"
        return cadena.format(self.NroAula, self.Piso, self.Capacidad)

    def __str__(self):
        return self.CapacidadAulas()


class Asignacion(models.Model):
    Cursadas = models.ForeignKey(
        Cursadas, null=False, blank=False, on_delete=models.CASCADE)
    Aulas = models.ForeignKey(
        Aulas, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Cursadas, self.Aulas)
