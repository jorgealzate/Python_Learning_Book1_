#TUPLAS

#las tuplas son inmutables
#son parecidas a las listas
#pueden ser valores de cualquier tipo
#las tuplas son comparables y dispersables (hashables) se pueden ordenar
#se pueden usar como valores para las claves en los diccionarios
"""
t = 'a', 'b', 'c', 'd','e' #es opcional encerrar en parentesis
print(t)
print(type(t))
"""

#crear una tupla con unico elemento se incluye una coma al final
"""
t1 = ('a',)
print(type(t1))
"""

#usando funcion interna tuple() para crear una tupla
"""
t = tuple
print(type(t))
"""
#si el argumento es una secuencia(cadena, lista o tupla )
#el resultado es una tupla con los elementos
"""
t = tuple('altramuces')
print(t)
"""

#la mayoria de los operadores de listas funcionan como tuplas
"""
t = ('a', 'b', 'c', 'd','e')
print(t[0])
#el operador de rebanada slice selecciona un rango de elementos 
print(t[1:3])
#no se puede modificar los elementos ERROR t[0] = 'A'
#pero se puede reemplazar una tupla por otra
t = ('A',) + t[1:]
print(t)
"""

#comparacion de tuplas
#los operadoores de comparacion funcionan tiembien con las tuplas
"""
print((0,1,2) < (0,3,4))
#salida True
"""

#funcion sort()
"""
txt = 'pero que luz se deja ver alli'
palabras = txt.split()
t = list()
#bucle que crea una lista de tuplas
for palabra in palabras:
    t.append((len(palabra),palabra))

t.sort(reverse=True)#reverse indica que debe ir en orden decreciente

#bucle que recorre la lista de tuplas
res = list()
for longitud, palabra in t: #dos variables por que es tupla
    res.append(palabra)

print(res)
"""

#Asignacion de Tuplas
#tener una tupla en el lado izquierdo de una sentencia de asignacion 
#esto permite asignar varias variables el mismo tiempo cuando 
#tenemos una secuencia en el lado izquierdo
"""
m = ['pasalo', 'bien']
x, y = m
print(x)
print(y)

#es lo mismo que decir 
x = m[0]
y = m[1]
print(x)
print(y)

#es lo mismo que decir 
(x, y) = m
print(x)
print(y)

#usuario y dominio
dir = 'monty@python.org'
usuario, dominio = dir.split('@')
print(usuario)
print(dominio)
"""

#Diccionarios Tuplas
#metodo items() que devuelve una lista de tuplas 
#cada una es una pareja de clave valor 
#igual los elementos no tienen ningun orden
"""
d =  {'a':10, 'b':1, 'c':22 }
t = d.items()
print(t)
#pero podemos ordenar las listas y las tuplas son comparables 
t.sort() #con python27
print(t)
"""

#Asignacion multiple con diccionarios
"""
d =  {'a':10, 'b':1, 'c':22 }
l = list()
for clave,valor in d.items():
    l.append((valor,clave))

l.sort(reverse=True)
print(l)
"""

#las palabras mas comunes 
#imprimir las 10 palabras mas comunes de un texto
#use python3
"""
import string
manf = open('romeo-full.txt')
contadores = dict()
for linea in manf:
    linea = linea.translate(string.punctuation)
    linea = linea.lower()
    palabras = linea.split()

    for palabra in palabras:
        if palabra not in contadores:
            contadores[palabra] = 1
        else:
            contadores[palabra] += 1
    
#ordenar el diccionario por valor 
lst = list()
for clave, valor in contadores.items():
    lst.append((valor, clave))

lst.sort(reverse=True)

for clave, valor in lst[:10]:
    print(clave, valor)
"""

#uso de tuplas en diccionarios
#dado que las tuplas son inmutables no proporcionan
#metodos como sort y reverse, sin embargo python 
#proporciona funcionen integradas como sort y reverse que toman una 
#secuencia como parametro y devuelven una secuencia nueva con los mismo elementos 
#en un orden diferente 

#DSU : decorate-sort-undecorate decorar ordenar y quitar 
#un diseno que implica construir una lista de tuplas, ordenar y extraer parte
#del resultado 
#Singleton: una lista u otra secuencia con un unico elemento


#ejercicio 10.11
"""
manf = open('mbox-short.txt')
lst = list()
usuario = dict()
#bucle que llena un diccionario con usuarios y su cantidad
for linea in manf:
    if linea.startswith('From '):
        lst = linea.split()
        if lst[1] not in usuario:
            usuario[lst[1]] = 1
        else:
            usuario[lst[1]] += 1

#bucle que recorre el diccionario y muesrta su clave y valor   
for clave, valor  in usuario.items():
    print(clave, '---->', valor)
"""











