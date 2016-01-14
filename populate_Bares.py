# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoP4.settings')

import django
django.setup()

from Bares.models import Bar, Tapa


def populate():
	barestapas = addBar(nombre="La Posada", lema="Desayunos y tapas todos los dias", descripcion="Bar acogedor en el que puedes tomar desayunos, tapas, copas... Disponemos de terraza todo el año", direccion="calle periodista", visitas=0)
	addTapa(nombrebar= barestapas, titulo = "montadito de lomo", descripcion = "bocadillo de lomo con lechuga y mayonesa")
	addTapa(nombrebar= barestapas, titulo = "piza york", descripcion = "porcion de piza de york")
	addTapa(nombrebar= barestapas, titulo = "piza atun", descripcion = "porcion de piza de atun")

	barestapas = addBar(nombre="Rialca", lema="Tenemos de todo y todo muy bueno",descripcion="Bar granadino de barrio en el que te sentirás como en casa. Gran proyetor para ver los partidos de tu equipo. Una excelente cocina", direccion="Avenida Andalucia", visitas=0)
	addTapa(nombrebar= barestapas, titulo = "montadito de lomo", descripcion = "bocadillo de lomo con tomate y jamón")
	addTapa(nombrebar= barestapas, titulo = "carne en salsa", descripcion = "plato de carne en salsa de la casa")
	addTapa(nombrebar= barestapas, titulo = "piza atun", descripcion = "porcion de piza de atun")

	barestapas = addBar("Ecu", "Todo a lo grande", descripcion= "Cervecería Estrella Galicia. Yo pido la tapa por ti y sé que no me rechistarás", direccion="Avenida estado los cármenes", visitas=0)
	addTapa(nombrebar= barestapas, titulo = "montadito de lomo", descripcion = "bocadillo de lomo con tomate y jamón")
	addTapa(nombrebar= barestapas, titulo = "carne en salsa", descripcion = "plato de carne en salsa de la casa")
	addTapa(nombrebar= barestapas, titulo = "perrito", descripcion = "hot dog extra grande")

    # Print out what we have added to the user.
	for b in Bar.objects.all():
		for t in Tapa.objects.filter(nombrebar=b):
			print "- {0} - {1}".format(str(b), str(t))

def addTapa(nombrebar, titulo, descripcion):
    p = Tapa.objects.get_or_create(nombrebar=nombrebar, titulo=titulo, descripcion= descripcion)[0]
    return p

def addBar(nombre, lema, descripcion, direccion, visitas):
    c = Bar.objects.get_or_create(nombre=nombre, lema=lema, descripcion=descripcion, direccion=direccion, visitas=visitas)[0]
    return c



# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()