# Automatizacion de tareas habituales en tu pc

# os.walk o for: para movernos a traves de todos los directorios y archivos
# socket : usar un bucle para leer el contenido de una conexion de red
# open :permite usar un bucle para leer el contenido de un archivo
# urllib :permite abrir un documento web y movernos a traves de su contenido

# delvuelve el nombre del directorio actual
# modulo os proporciona funciones para trabajar con archiovs y directorios
# os de operating system
# cwd significa current workind directory

"""
import os
cwd = os.getcwd()
print cwd
"""

"""
#ruta absoluta
import os
os.path.abspath('tmp.txt')
#comprueba si el fichero existe
x = os.path.exists('tmp.txt')
print x #salida :sea True o False
#comprueba si se trata de un directorio
x = os.path.isdir('tmp.txt')
print x #salida :sea True o False
#comprueba si se trata de un fichero 
x = os.path.isfile('tmp.txt')
print x #salida :sea True o False
"""

"""
#devuelve una lista de ficheros o directoriso en el directorio dado
import os
cwd = os.getcwd()
lst = os.listdir(cwd)
for elemt in lst:
    print elemt
#o tambien puede ser facilmente 
print lst
"""

"""
#inventario de cuantos archivos de texto hay en directorio y subdirectorios
#os.walk recorre en todos los subdirectorios y directorio actual
import os
contador = 0
for (nombredir,dirs,ficheros) in os.walk('.'):
    for nombrefichero in ficheros:
        if nombrefichero.endswith('.txt'):
            contador = contador + 1
print 'Cantida de .txt : ', contador
"""

# imprime los nombres de los ficheros con extension .txt
"""
import os 
from os.path import join
for (nombredir,dirs,ficheros) in os.walk('.'):
    for nombrefichero in ficheros:
        if nombrefichero.endswith('.txt'):
            elfichero = os.path.join(nombredir,nombrefichero)
            print os.path.getsize(elfichero), elfichero
"""


# busca los ficheros que tengan mas de una linea de longitud y muestre contenido
"""
import os
from os.path import join
for (nombredir, dirs, ficheros) in os.walk('.'):
    for nombrefichero in ficheros:
        if nombrefichero.endswith('.txt'):
            elfichero = os.path.join(nombredir, nombrefichero)
            tamano = os.path.getsize(elfichero)
            if tamano == 2578 or tamano == 2565:
                continue #omite ficheros de tamanos incorrectos
            manf = open(elfichero,'r')
            lineas = list()
            for linea in manf:
                lineas.append(linea)
            manf.close()
            if len(lineas) > 1:
                print len(lineas), elfichero
                print lineas[:4]
"""

# imprimir ficheros que estan a punto de ser eliminados
"""
import os
from os.path import join
for (nombredir, dirs, ficheros) in os.walk('.'):
    for nombrefichero in ficheros:
        if nombrefichero.endswith('.txt'):
            elfichero = os.path.join(nombredir, nombrefichero)
            tamano = os.path.getsize(elfichero)
            if tamano == 2578 or tamano == 2565:
                print 'T-Mobile:', elfichero
                #os.remove(elfichero) elimina el fichero
                continue
            manf = open(elfichero, 'r')
            lineas = list()
            for linea in manf:
                lineas.append(linea)
            manf.close()
            if len(lineas) == 3 and lineas[2].startswith('Sent from my iPhone'):
                print 'iPhone:', elfichero
                #os.remove(elfichero) elimina el fichero
                continue
"""


#LECTURA DE ARGUMENTOS DESDE UNA LINEA DE COMANDO
"""
import sys
print 'Cantidad: ', len(sys.argv)
print 'Tipo: ', type(sys.argv)
for arg in sys.argv:
    print 'Argumento: ', arg
"""
#podemos leer ficheros tomando el nombre de este fichero 
#cap16_Automat_tarea_PC.py junto al fichero a leer
#desde un argumento de linea de comando:
"""
import sys
nombre = sys.argv[1]
manejador = open(nombre, 'r')
texto = manejador.read()
print nombre , 'tiene ', len(texto), 'bytes'
"""
#se usa asi en la consola :
#cap16_Automat_tarea_PC.py mbox-short.txt
#la salida es:
#mbox-short.txt tiene  94626 bytes
#esto sin necesidad de usar :
#nombre = raw_input('Introduzca fichero:')
#manejador = open(nombre, 'r')
#texto = manejador.read()


#PIES - tuberias
#cualquier programa que se ejecute desde Shell puede ser 
#ejecutado tambien en python usando pipe: una tuberia es 
#un objeto que representa a un proceso en ejecucion
import os
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print stat