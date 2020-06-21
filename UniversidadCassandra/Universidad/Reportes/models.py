from django.db import models

# Create your models here.
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class reporte(DjangoCassandraModel):
    rpt_id     = columns.Integer(primary_key=True, required=True)
    rpt_nombre = columns.Text(required=False)
