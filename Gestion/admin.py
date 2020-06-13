from django.contrib import admin

from Gestion.models import Cursadas, Aulas, Asignacion

# Register your models here.


class CursadasAdmin(admin.ModelAdmin):
    list_display = ("NombredeMateria", "Carrera", "CantidadAlumnos")
    search_fields = ("NombredeMateria", "Carrera", "CantidadAlumnos")


admin.site.register(Cursadas, CursadasAdmin)
admin.site.register(Aulas)
admin.site.register(Asignacion)
