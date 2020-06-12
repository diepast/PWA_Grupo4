from django.contrib import admin

from Gestion.models import Cursadas, Aulas

# Register your models here.


class CursadasAdmin(admin.ModelAdmin):
    list_display = ("Carrera", "NombredeMateria", "CantidadAlumnos")
    search_fields = ("Carrera", "NombredeMateria", "CantidadAlumnos")


admin.site.register(Cursadas, CursadasAdmin)
admin.site.register(Aulas)
