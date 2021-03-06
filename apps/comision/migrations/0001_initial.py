# Generated by Django 3.0.7 on 2020-06-20 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='turno',
            fields=[
                ('idTurno', models.CharField(choices=[('T', 'Tarde: 13:00 a 19:00'), ('N', 'Noche: 19:00 a 23:00')], default='N', max_length=1, primary_key=True, serialize=False)),
                ('NroAula', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aula.aula')),
            ],
        ),
        migrations.CreateModel(
            name='comision',
            fields=[
                ('idComision', models.CharField(choices=[('1A', 'Comision_1A'), ('1B', 'Comision_1B'), ('2A', 'Comision_2A'), ('2B', 'Comision_2B'), ('3A', 'Comision_3A'), ('3B', 'Comision_3B'), ('4A', 'Comision_4A'), ('4B', 'Comision_4B')], default='1A', max_length=2, primary_key=True, serialize=False)),
                ('idTurno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comision.turno')),
            ],
        ),
    ]
