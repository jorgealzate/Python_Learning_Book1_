"""
Expresiones regulares: libreria potente analisis de textos
Esta tarea de buscar y extraer es tan comun que Python tiene una libreria muy potente
llamada expresiones regulares, que se encarga de muchas de estas tareas de
forma elegante.

import re
try:
    manf = open('mbox-short.txt')
except:
    print ' el texto no se encontro'
    exit()
#salida de lineas que solo empiecen con From:
for linea in manf:
    linea = linea.rstrip()
    if re.search('From:',linea):
        print linea

#el caracter para indicar el comienzo de una linea
import re
try:
    manf = open('mbox-short.txt')
except:
    print ' el texto no se encontro'
    exit()
for linea in manf:
    linea = linea.rstrip()
    if re.search('^From:',linea):
        print linea

#equivalencia de caracteres
#donde un punto equivale a cualquier caracter
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if re.search('^F..m:', linea):
        print linea


#restringir mas lineas que coincidan con la 
#busqueda
# busca From seguido con uno o mas caracteres seguidos 
#de un simbolo @
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if re.search('^From:.+@',linea):
        print linea


#extraccion de datos 
#se usa findall() para localizar lineas que contienen
#direcciones de e-mail y extrae mas direcciones
#\S+ equivale a tantos caracteres no-espacio-en-blanco como sea posible
import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu ahout the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print lst
#salida asi :
#['csev@umich.edu', 'cwen@iupui.edu']

import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    x = re.findall('\S+@\S+', linea)
    if len(x) > 0:
        print x

#salida asi:
# ['<source@collab.sakaiproject.org>;']
#debemos quitar el < y ;
#usaremos la siguiente expresion regular 
# '[a-zA-Z0-9]\S*@\S*[a-zA-Z]'
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', linea)
    if len(x) > 0:
        print x
# salida asi :
# ['source@collab.sakaiproject.org']
   
#encontrat numeros que comienzan con la
#cadena X-
# como algo asi X-DSPAM-Confidence: 0.8475
# usaremos la siguiente expresion regular
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if re.search('^X\S*: [0-9.]+', linea):
        print linea
#salida asi :
# X-DSPAM-Confidence: 0.8475
#pero ahora necesitamos solo los numeros

#anadimos parentisis a la expresion regular 
#que represneta el numero punto flotante
#este parentesis le dice a la funcion findall()
# que devuelva solo lo del parentesis
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', linea)
    if len(x) > 0:
        print x
#salida asi :
# ['0.8475'] 
#aqui solo falta convertir a punto flotante

#si queremos extrar los numeros de revision
#buscamos lineas que comiencen con Details 
#seguido de cualquier numero de caracteres *
#por rev= y luego por uno o mas digitos
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', linea)
    if len(x) > 0:
        print x    
#salida asi :
#['39770']

# extraemos algo asi solo los numeros de :
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
import re
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    x = re.findall('^From .* ([0-9][0-9])',linea)
    if len(x) > 0:
        print x
"""

#escapado de caracteres es:
#en este ejemplo cogemos 
#un numero junto a un punto y 
# seguido de un caracter especial en este 
#caso $
"""
import re
x = 'Acabamos de recibir 10.00$ por las galletas.'
y = re.findall('[0-9.]+\$',x)
print y
#salida asi :
#['10.00$']
"""

