from django.db import models

# Create your models here.
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class cursada(DjangoCassandraModel):
    id        = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    materia   = columns.Text(required=False)
    carrera   = columns.Text(required=False)
    comision  = columns.Text(required=True)
    turno     = columns.Text(required=True)
    q_alumnos  = columns.Integer(required=False)


class aula(DjangoCassandraModel):
    id           = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    nro          = columns.Integer(required=False, index=True)
    piso         = columns.Text(required=False)
    capacidad    = columns.Integer(required=False)


class carrera(DjangoCassandraModel):
    id     = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    nombre = columns.Text(required=False)


class materia(DjangoCassandraModel):
    id      = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    nombre  = columns.Text(required=False, index=True)
    carrera = columns.Text(required=False)


class turno(DjangoCassandraModel):
    id          = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    descripcion = columns.Text(required=False)


class comision(DjangoCassandraModel):
    id          = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    descripcion = columns.Text(required=False)


class dia(DjangoCassandraModel):
    id     = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    nombre = columns.Text(required=False)


class asignacion(DjangoCassandraModel):
    id         = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    aula_id    = columns.Integer(required=True)
    cursada_id = columns.Integer(required=True)


#  myapp/models.py
#import uuid
#from cassandra.cqlengine import columns
#from django_cassandra_engine.models import DjangoCassandraModel

#class ExampleModel(DjangoCassandraModel):
#	example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
#	example_type = columns.Integer(index=True)
#	created_at   = columns.DateTime()
#	description  = columns.Text(required=False)