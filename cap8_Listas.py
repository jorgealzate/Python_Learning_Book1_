#listas

#las listas son mutables 
#se pueden cambiar 
#pueden ser de cualquier tipo
#los valores reciben el nombre de elementos o articulos

#mode de crear lista con [ ]
"""
print [10, 20, 30, 40]
print ['rana', 'vejiga', 'vomito']
print ['spam', 2.0, 5, [10, 20]]#hay una lista dentro de una lista

#se asigna listas a variables 
quesos = ['cheddar', 'Edam', 'Gouda']
numeros = [17, 123, 45, 80]
vacia =[]
print quesos, numeros, vacia

#para acceder a los elementos es lo mismo que en las cadenas 

print quesos[0]
print numeros[1]

#las listas son mutables
#relacion entre indices y elementos , llamado mapeo o direccionamiento
#los indices funcional del mismo modo que una cadena
numeros[1] = 5
print numeros
"""


#operador in en la lista, devuelve True o False 
"""
print 'Edam' in quesos
"""

#recorrer una lista 
#modo habitual es con for , sintaxis igual que las cadenas
"""
for queso in quesos:
    print queso
"""

#si necesita modificar necesitaras los indices
"""
for i in range(len(numeros)):#range devuelve una lista de indices desde 0 hasta n-1
    numeros[i] = numeros[i] * 2
print numeros
"""


#una lista contiene otras listas pero estas listas anidades 
#contiene un unico elemento
"""
lst = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for elemento in lst:
    print elemento
"""

#operadores con listas
"""
a = [1 ,2, 3]
b = [4, 5, 6]
c = a + b
print c

d = [0] * 4
print d
"""

#rebanando listas
#usando rebanador slice
"""
t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[1:3]
print t[:4]#si omites el primer indice rabana desde el principio
print t[3:]#si omites el segudno indice llegara hasta el final
"""

#como las listas son mutables, resulta util hacer una copia 


#metodos de listas
#anade un nuevo elemento append()
"""
t = ['a', 'b', 'c']
t.append('d')
print t
"""


#extend() toma una lista con argumentos y anade al final de la actual 
"""
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print t1
"""

#ordena una lista con sort()
"""
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print t
"""


#elimina un elemento de la lista pop() pero se puede guardar en una variable
"""
t = ['d', 'c', 'e', 'b', 'a']
x = t.pop(1)
print t
print x
"""


#elimina definitivament un elemento de lista
"""
t = ['d', 'c', 'e', 'b', 'a']
del t[1] #el valor que devuelve del es None
print t
"""


#si se conoce el elemento pero no su indice se
#usa remove
"""
t = ['d', 'c', 'e', 'b', 'a']
t.remove('b')
print t
"""


#para eliminar mas de un elemento usar del 
#con indice de rebanada
"""
t = ['d', 'c', 'e', 'b', 'a']
del t[1:3]#rebana desde el 1 pero no incluye el 3
print t
"""

#listas y funciones  internas
"""
nums = [3, 41, 12, 9, 74, 15]
print len(nums)#el tamano de la lista
print max(nums)#numero mayor en la lista
print min(nums)#numero menor en la lista
print sum(nums)#suma de la lista
print sum(nums) / len(nums)#divide la suma y el tamano de la lista
"""

#calcula la media de varios numeros introducidos 
"""
total = 0
contador = 0
while True:
    ent = raw_input('ingrese un numero: ')
    if ent == 'fin' : break
    valor = float(ent)
    total = total + valor 
    contador = contador + 1

media = total / contador
print 'media : ', media 
"""

#ahora hagamoslo con una lista
"""
listnum = list()
while True:
    ent = raw_input('ingrese un numero: ')
    if ent == 'fin' : break
    valor = float(ent)
    listnum.append(valor)

media = sum(listnum) / len(listnum)
print 'Media: ', media
"""

#listas y cadenas
#convertir una cadena a lista
#vidide una cadena letra por letra con list()
"""
s = 'spam' #cadena
t = list(s)
print t
"""

#dividir la cadena en palabras con split() 
"""
s = 'susupirando por los fiordos'
t = s.split()
print t
"""

#usando split para dividir la cadena con un delimitador
"""
s = 'spam-spam-spam-spam'
delimitador = '-'
s.split(delimitador)
print s
print type(s)
"""
#pero sigue siendo cadena


#pasa a ser una lista 
"""
fx = '2x^2+3x+3'
delimitador = '+' 
t = fx.split(delimitador) #pasa a ser una lista
print t
print type(t)
"""

#la inversa de split() es join()
#la lista pasa a ser cadena unida 
#si el delimitar es ' ' lo une con eso 
#probar con delimitador sea '+'
"""
t = ['suspirando', 'por', 'los', 'fiordos']
delimitador = ' '
nuevaCadena = delimitador.join(t)
print nuevaCadena
print type(nuevaCadena)#
"""

#Analisis de Lineas
#analizar o parsear cada linea para obtener cierta parte
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if not linea.startswith('From ') : continue
    palabras = linea.split()
    print palabras[2]
"""

#objetos y valores
#has copias para no tener problemas si usas alias 
"""

#en dos cadenas son iguales 
a = 'banana'
b = 'banana'
print a is b
#salida : True

#pero en dos listas son objetos distintos
a = [1, 2, 3]
b = [1, 2, 3]
print a is b
#salida False

#alias
a = [1, 2, 3]
b = a
print b is a
#salida True
#si es mutable un objeto alias el otro tambien cambia
b[0] = 17
print a
#es algo util pero propenso a errores
"""

#listas como Argumentos 
#si la funcion modifica un parametro de la lista . el codigo 
#que la ha llamado tambien se vera afectado por el cambio

"""
def borra_primer(t):
    del t[0]

letras = ['a', 'b', 'c']
borra_primer(letras)
print letras 
"""

#appedn() modifica una lista
"""
t1 = [1, 2]
t2 = t1.append(3) #solo devuelve None asi que no necesita variable
print t1
print t2
"""

# + crea una nueva lista
"""
t3 = t1 + [3]
print t3
print t1
"""

#funcion que devuelve todos los elementos excepto el primero 
"""
def cola(t):
    return t[1:]

letras = ['a', 'b', 'c']
resto = cola(letras)
print resto
"""

#ejercicio 8.1
"""
def recortar(t):
    del t[0]
    del t[len(t) - 1]

def centro(t):
    t.pop(0)
    t.pop(len(t) - 1)    
    return t

def centro_rebanado(t):
    s = t[1:len(t)- 1]
    return s

i = [1, 2, 3, 4, 5]
print recortar(i)
print i

f = [1, 2, 3, 4, 5]
print centro(f)

g = [1, 2, 3, 4, 5]
print centro_rebanado(g)
"""

#haz una copia de la lista para evitar los alias 
"""
t = [2, 1, 5, 4, 3]
orig = t[:] #saca una copia para evitar alias
t.sort()
print orig
print t 
"""

#ejercicio 8.4

manf = open('romeo.txt')
lst = list()
for linea in manf:
    palabras = linea.split()
    if len(palabras) == 0 : continue
    else:
        lst.append(palabras)
        print linea
print lst
