#PROGRAMAS EN RED

#fingeremos se un navegador wed y recuperamos 
#paginas web usando el prtocolo de Transporte
#de Hypertexto
#HypertText transport Protocol HTTP
#soporte integrado en python : sockets
#hace conexion de red y recuperar datos
#el socket proporciones conexion de doble sentido
#entre dos programs
#se lee y se escribe en el mismo socket
#si se lee en un socket se obtiene los datos que 
#la otra aplicacion ha enviado
#informacion en :
#http://www.w3.org/Protocols/rfc2616/rfc2616.txt
#en la pagina 36 del RFC2616 encontrara 
#las sintasis para las peticiones GET.

#realiza conexion con un servidor web y siga 
#las reglas de ese protocolo para solicitar un documento
#y mostrar lo que el servidor devuelve
"""
import socket

misochet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misochet.connect(('www.py4inf.com',80))
misochet.send('GET /code/romeo.txt HTTP/1.0\nHost: www.py4inf.com\n\n')
while True:
    datos = misochet.recv(512)
    if (len(datos) < 1):
        break
    print datos

misochet.close()
"""


#recepcion de una imagen mediante HTTP
"""
import socket
import time

misocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misocket.connect(('www.py4inf.com', 80))
misocket.send('GET /cover.jpg HTTP/1.0\nHost: www.py4inf.com\n\n')
contador = 0
imagen ="";
while True:
    datos = misocket.recv(5120)
    if (len(datos) < 1 ): break
    # time.sleep(0.25)
    contador = contador + len(datos)
    print len(datos), contador
    imagen = imagen + datos

misocket.close()


# busqueda del final de la cabecera (2 CRLF)

pos = imagen.find("\r\n\r\n");
print 'tamano de cabecera', pos
print imagen[:pos]

#salta detras de la cabecera y guardar los datos de la imagen
imagen = imagen[pos+4:]
manf = open("cosa.jpg","wb")
manf.write(imagen);
manf.close()
"""

#recepcion de pagina web con urllib
#urllib es una libreria de python mas sencilla 
#trae una pagina web mucho mas parecida a un ficherp
"""
import urllib

manf = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#lo trae como archivo y luego se lee
for linea in manf:
    print linea.strip()


#programa que recupera datos web y calcula la cantidad 
#de cada palabra del fichero:
import urllib
contadores = dict()#diccionario 
manf = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for linea in manf:
    palabras = linea.split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabra,0) + 1
print contadores
"""

#analisis de HTML mediante expresiones regulares
#ver la expresion regular en el codigo:
#esta expresion regular busca cadenas que comiencen por href  y
#seguido de uno o mas caracteres 
#seguidos por la comilla doble
#el signo de interrogacion  indica que la coincidencia debe ser 
#hecha en modo no-codicioso. 
#el metodo findall proporciona lista de todas las cadenas 
#coinciden con la expresion regular, devolviendo solo el texto 
#del enlace situado dentro de las comillas dobles
"""
import urllib
import re
url = 'http://www.py4inf.com/book.htm'
html = urllib.urlopen(url).read()
enlaces = re.findall('href="(http://.*?)"', html)
for enlace in enlaces:
    print enlace
"""

#analisis de HTML mediante libreriao BeautifulSoup
#este libreria se puede descargar e instalar desde:
#http://www.crummy.com/software/
#o simplemente colocar el archivo de BeutifulSoup.py en la 
#misma carpeta de la aplicacion
#para instalar esta librerias necesitas tenet Pypi
#instala python 2.7.17 que ya tiene pypi
#abres la consola y escribes para instalar:
#pip install beautifulsoup4

import urllib
from BeautifulSoup import *
url = 'http://www.py4inf.com/book.htm'
html = urllib.urlopen(url).read()
sopa = BeautifulSoup(html)
#recuerda todas las etiquetas de anclaje
etiquetas = sopa('a')
for etiqueta in etiquetas:
    print (etiqueta.get('href', None))


#lectura de archivos binarios mediante urllib
#de archivos pequenos
#como un archivo de imagen o video 
"""
import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
manf = open('portada.jpg', 'wb')
manf.write(img)
manf.close()
"""

#lectura de archivos binarios mediante urllib
#de archivos grandes
# en unix seria 
# curl -O http://www.py4inf.com/cover.jpg
"""
import urllib
img =urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
manf = open('portada.jpg','wb')
tamano = 0
while True:
    info = img.read(100000)
    if len(info) < 1 : break
    tamano = tamano + len(info)
    manf.write(info)
print tamano, 'caracteres copiados'
manf.close()
"""