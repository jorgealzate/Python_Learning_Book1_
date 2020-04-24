#apertura de ficheros
#primero se debe abrir el fichero 
#archivo de ejemplo en :
#http://www.py4inf.com/code/mbox.txt
#version reducida en :
#http://www.py4inf.com/code/mbox-short.txt
"""
manf = open('mbox.txt')
print manf
"""
#salida : <open file 'mbox.txt', mode 'r' at 0x0000000002D94030>
#nos devuelve un manejador de fichero --handle
#el handle usa , open, read, write, close 
#caracter de salto de linea es \n

#cuenta cuatas lineas tiene el archivo de texto 
"""
manf = open('mbox-short.txt')
contador = 0 
for linea in manf:
    contador = contador + 1
print 'lineas contabilizadas: ', contador
"""
#usando funcion interna
#la longitud del archivo
"""
manf = open('mbox-short.txt')
ent = manf.read()
print len(ent)
print ent[:20]#muestra los primeros 20 caracteres
"""
#lo anterior dado para archivos pequenos 
#si el archivo no cabe en la memoria lo mejor es hacerlo por bloque 
#usando bucle for o while

#busqueda dentro de un fichero
#seleccionar solo las lineas que empiezan con From
"""
manf = open('mbox-short.txt')
for linea in manf:
    if linea.startswith('From'):
        print linea
"""
#pero la salida esta con linea vacias debido al salto de lineas
#usamos rstrip() que elimina los espacios en blanco
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if linea.startswith('From'):
        print linea
"""
#lo mismo que lo anterior pero 
#saltar las lineas que no interesan
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    #saltar lineas que no interesan
    if not linea.startswith('From:'):
        continue
    #procesar linea interesante
    print linea 
"""

#mostrar las lineas que son de @uct.ac.za
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1:
        continue
    print linea 
"""

#permientiendo que ingrese el nombre del fichero
"""
nombref = raw_input('introduzca el nombre del fichero: ')
manf = open(nombref)
contador = 0
for linea in manf:
    if linea.startswith('Subject:'):
        contador = contador + 1
print 'Hay', contador, 'linea Subject en ', nombref
"""

#uso de Try Except y open
"""
nombref = raw_input('ingrese el nombre del fichero: ')
try:
    manf = open(nombref)
except:
    print 'no se pudo abrir el fichero: ', nombref
    exit()

contador = 0
for linea in manf:
    if linea.startswith('Subject:'):
        contador = contador + 1
print 'Hay ', contador, 'lineas Subject en ', nombref
"""

#escritura de ficheros
#si el fichero ya existe , eliminara el fichero antiguo
#tambien se deben cerrar ficheros de solo lectura pero en caso de muchos 

fsal = open('salida.txt', 'w')
print fsal
linea_1 = 'Aqui esta el zarzo\n'
linea_2 = 'El simbolo de nuestra tierra.\n'
fsal.write(linea_1)
fsal.write(linea_2)
contador = 0
#escribe numeros hasta el 30
while contador < 30:
    contador = contador + 1
    fsal.write(str(contador)+'\n')
fsal.close()#cerrar el fichero


