from django.contrib import admin

from Gestion.models import cursada, aula, carrera, materia, turno, comision, dia, asignacion

# Register your models here.

admin.site.register(cursada)
admin.site.register(aula)
admin.site.register(carrera)
admin.site.register(materia)
admin.site.register(turno)
admin.site.register(comision)
admin.site.register(dia)
admin.site.register(asignacion)