#diccionarios

#use python 3 debido a carateres unicode

#en los diccionarios los indices pueden ser 
# de cualquier cosa
#cada clave (indice) apunta a un valor 
#pareja clave valor 
"""
eng2sp = dict()
print eng2sp
"""

#anadir elementos al diccionario
"""
eng2sp['one'] = 'uno'
print eng2sp
"""

#el formato de salida { } tambien es de entrada
"""
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print eng2sp
"""
#pero en la salida el orden no es el mismo 
#el orden de los elementos en un diccionario es impredecible
#los elementos de un diccionario nunca son indexados
#en lugar se usa las claves para buscar valores
"""
print eng2sp['two']
"""

#si la clave especificad no esta en el diccionario se obtiene una excepcion
#la funcion len() funciona en los diccionarios
"""
print len(eng2sp)
"""

#el operador in tambien funcionar en los diccionarios
"""
print 'one' in eng2sp
"""

#para ver si algo aparece como valor en un diccionario 
#se usa el metodo values()
"""
vals = eng2sp.values()
print 'uno' in vals
#salida True
"""


#el operador in :
#para las listas usa algoritmo lineal de busqueda 
#entre mas larga la lista  el tiempo de busqueda demora mas 
#para los diccionarios usa tabla de dispersion
#emplea la misma cantida de tiempo sin importar cuantos elementos hay
#es.wikipedia.org/wiki/Tabla_hash

#ejercicio 9.1
"""
manf = open('words.txt')
text = manf.read()
words = text.split()
d = dict()
cont = 1
for word in words:
    d[cont] = word
    cont = cont + 1
print d
"""

#diccionario como conjuntos de contadores
#es como hacer un histograma
"""
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d) #en python 3 ya va dentro (x) pero tambien funciona en python2.7
"""

#funcion interna get() que toma una clave o un valor por defecto 
#si la clave esta en el diccionario devuelve el valor 
#si no devuelve el valor por defecto 
"""
contadores = {'chuck':1, 'annie':42, 'jan':100}
print(contadores.get('jan',0))
"""
#usando get() para recuento
#estilo que se usa con mucha frecuencia

"""
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    d[c] = d.get(c,0) + 1
print(d)
"""

#diccionarios y archivos
#contar la aparicion de palabras en un archivo
#usando bucles aninados
#pero la salida es un conteo sin ordenar
"""
manf = open('romeo.txt')
contadores = dict()
for linea in manf:
    palabras = linea.split()#elimina los espacios
    for palabra in palabras:
        if palabra not in contadores:
            contadores[palabra] = 1
        else:
            contadores[palabra] += 1

print(contadores)
"""

#encontrar todas las entradas de diccionario que sean mayor de 10
"""
contadores = {'chuck':1, 'annie':42, 'jan':100}
for clave in contadores:
    if contadores[clave] > 10:
        print(clave, contadores[clave])
"""

#proceso avanzado de texto
#usando string.translate(s, table[, deletechars])
#dado que no solo hay espacios vacios sino tambien signos de puntuacion, 
#signos de admiracion , signos de pregunta 
"""
import string
print(string.punctuation)
#salida !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ use python3
"""

"""
#use python 3
import string
manf = open('romeo.txt')
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

print(contadores)
"""

#ejercicio 9.2
"""
manf = open('mbox-short.txt')
lst = list()
dias = dict()
for lineas in manf:
    if lineas.startswith('From '):
        lst = lineas.split()
        print(lst)
        if lst[2] not in dias:
            dias[lst[2]] = 1
        else:
            dias[lst[2]] += 1
print(dias)
"""
        
            





