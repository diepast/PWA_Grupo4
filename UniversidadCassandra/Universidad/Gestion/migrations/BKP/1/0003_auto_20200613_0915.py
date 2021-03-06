# Generated by Django 3.0.6 on 2020-06-13 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_auto_20200612_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursadas',
            name='Carrera',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cursadas',
            name='NombredeMateria',
            field=models.CharField(max_length=45),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aulas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Aulas')),
                ('Cursadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Cursadas')),
            ],
        ),
    ]
