# Generated by Django 3.0.7 on 2020-06-18 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacion',
            name='Aulas',
        ),
        migrations.RemoveField(
            model_name='asignacion',
            name='Cursadas',
        ),
        migrations.RemoveField(
            model_name='asignacion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='aulas',
            name='Capacidad',
        ),
        migrations.RemoveField(
            model_name='aulas',
            name='NroAula',
        ),
        migrations.RemoveField(
            model_name='aulas',
            name='Piso',
        ),
        migrations.RemoveField(
            model_name='aulas',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='CantidadAlumnos',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='Carrera',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='Comision',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='NombredeMateria',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='Turno',
        ),
        migrations.RemoveField(
            model_name='cursadas',
            name='id',
        ),
    ]
