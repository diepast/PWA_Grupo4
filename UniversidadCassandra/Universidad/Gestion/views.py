from django.shortcuts import render

from django.db import connection

#from django.http import HttpResponse
#from django.http import HttpResponseRedirect

import uuid

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from cassandra.cluster import Cluster

from .models import aula
from .models import materia

from .forms import AulasForm
from .forms import MateriasForm


# Create your views here.

def index(request):
    context = {}
    return render(request, 'Gestion/index.html', context)


def aulas(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AulasForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            data 		= request.POST.copy() 		# Copia la data del post a la variable data, luego voy a extaer los campos del form con esta variable
            nro 		= data.get('nro') 			# aca extraigo los campos del form de la data que definimos en la linea anterior, el parentisis refiere al nombre que definimos el campo en el form.py
            piso 		= data.get('piso')
            capacidad 	= data.get('capacidad') 	# esto refiere al nombre que definimos en el form.py
            
            cluster 	= Cluster(['127.0.0.1'])
            session 	= cluster.connect()

            session.set_keyspace('db')

            query = "SELECT * FROM aula WHERE nro = {} ALLOW FILTERING;".format(nro)
            rows  = session.execute(query)
            
            existen = [] 			# CREO UN ARRAY
            for row in rows:
                existen.append(row) # LLENO EL ARRAY CON LAS FILAS

            cluster.shutdown() 		# Cierro La conexion

            if len(existen) > 0: 

                context = {'msj': "El aula nro {} ya existe".format(nro),'color':"red"}
                return render(request, 'Gestion/msj.html', context)

            else:
                #agregar un dia y crear las aulas x 5

                CrearAula(nro,piso,capacidad)
                cluster.shutdown() # Cierro La conexion

                context = {'form': form, 'msj': "El aula número {} se creó con éxito!".format(nro),'color':"green"}
                return render(request, 'Gestion/msj.html', context)

        # if a GET (or any other method) we'll create a blank form
    else:

        form = AulasForm()
        context = {'form': form}

    return render(request, 'Gestion/aulas.html', context)


def CrearAula(nro, piso, capacidad):
        NuevaAula 			= aula() 		# Instancio un objeto aula
        NuevaAula.id 		= uuid.uuid1()
        NuevaAula.nro 		= nro 			# asigno los valores del form en la prop del objeto instanciado en el paso anterior
        NuevaAula.piso		= piso
        NuevaAula.capacidad = capacidad 	# asigno los valores del form en la prop del objeto instanciado en el paso anterior
        NuevaAula.save() 					# salvo el objeto en la DB


def ListarAulas(request):
    ListaAulas = aula.objects.all()
    context = {'ListaAulas': ListaAulas}
    return render(request, 'Gestion/lista_aulas.html', context)


def materias(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MateriasForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            data 		= request.POST.copy() 		# Copia la data del post a la variable data, luego voy a extaer los campos del form con esta variable
            nombre 		= data.get('nombre') 		# aca extraigo los campos del form de la data que definimos en la linea anterior, el parentisis refiere al nombre que definimos el campo en el form.py
            carrera		= data.get('carrera')
            
            cluster 	= Cluster(['127.0.0.1'])
            session 	= cluster.connect()

            session.set_keyspace('db')

            query = session.prepare('SELECT * FROM materia WHERE nombre=? ALLOW FILTERING;')	#PREARMO LA QUERY EL ? SE REEMPLAZARA POR LAS VARIABLES
            rows = session.execute(query, [nombre]) 	# EJECUTO LA QUERY Y LE PASO LAS VARIABLES PARA FILTRAR IMPORTANTE QUE ESTEN ENTRE CORCHETES
            
            existen = [] 			# CREO UN ARRAY
            for row in rows:
                existen.append(row) # LLENO EL ARRAY CON LAS FILAS

            cluster.shutdown() 		# Cierro La conexion

            if len(existen) > 0: 

                context = {'msj': "La materia {} ya existe".format(nombre),'color':"red"}
                return render(request, 'Gestion/msj.html', context)

            else:
                #agregar un dia y crear las aulas x 5

                CrearMateria(nombre,carrera)
                cluster.shutdown() # Cierro La conexion

                context = {'form': form, 'msj': "La materia {} se creó con éxito!".format(nombre),'color':"green"}
                return render(request, 'Gestion/msj.html', context)

        # if a GET (or any other method) we'll create a blank form
    else:

        form = MateriasForm()
        context = {'form': form}

    return render(request, 'Gestion/materias.html', context)


def CrearMateria(nombre,carrera):
        NuevaMateria			= materia() 	# Instancio un objeto materia
        NuevaMateria.id 		= uuid.uuid1()
        NuevaMateria.nombre 	= nombre 		# asigno los valores del form en la prop del objeto instanciado en el paso anterior
        NuevaMateria.carrera	= carrera
        NuevaMateria.save() 					# salvo el objeto en la DB
