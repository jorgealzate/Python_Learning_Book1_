#CADENAS
#una cadena es una secuencia de caracteres
#se puede aceder de uno en uno o uno con [ ]
"""
fruta = 'banana'
letra = fruta[0]
print letra
"""


#obtener la longitud de una cadena 
"""
x = len(fruta)
print x
"""


#obtener la ultima letra
"""
ultima = fruta[x - 1]
print ultima
"""


#recorrido de una cadena 
#de izquierda a derecha
"""
indice = 0 
while indice < len(fruta):
    letra = fruta[indice]
    print letra
    indice = indice + 1
"""


#recorrido de una cadena 
#de derecha a izquierda
"""
indice = len(fruta)
while indice > 0:
    letra = fruta[indice-1]
    print letra
    indice = indice - 1
"""


#recorrido usando for 
"""
for letra in fruta:
    print letra
"""

#rebanado de cadenas
"""
s = 'Monty Python'
print s[0:5]
#salida : Monty
print s[6:12]
#salida : Python
print s[3:3]
"""


#salida ''  vacia, no contiene caracteres y longitud 0
#es un error decir que : 
# s[0] = 'j'
#eso no lo soporta por que las cadenas son INMUTABLES
#no se pueden cambiar 
#lo mejor es concatenar una cadena con otra
"""
x = 'Hola'
y = 'Carlos'
z = x + y
print z
"""

#bucles y contadores
#cuenta el numero de veces que aparece 'a' en una cadena 
"""
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print 'cantidad de letras a ', contador
"""
#ejercicio 6.3
"""
def contador( cadena, letra):
    contador = 0
    for caracter in cadena:
        if letra == caracter:
            contador = contador + 1
    return contador

ent = raw_input('ingrese cadena: ')
let = raw_input('ingrese letra: ')
x = contador(ent,let)
print 'cantidad de ', x
"""

#operador in
#devuelve verdadero o falso 
"""
fruta = 'banana'
print 'a' in fruta
"""
#salida : True


#comparacion de cadenas 
"""
fruta ='banana'
if 'banana' == fruta:
    print 'ok'
"""

#metodos de cadenas
#metodo dir que lista los metodos dispobles para un objeto
"""
cosa = 'Hola mundo que mas      '
print type(cosa)
print dir(cosa)
#puedes usar help para obtener un poco de informacion sobre cada metodo 
#https://docs.python.org/2/library/stdtypes.html#string-methods.
#invocamos el metodo upper() para convertir a mayusculas
print cosa.upper()#convierte a mayusculas

#invocamos el metodo find('x') que busca la posicion de una cadena dentro de otra
print cosa.find('a')
print cosa.find('co')
print cosa.find('mun')

#invocamos strip() para eliminar espacios en blanco
#tabulaciones, saltos de lineas
print cosa.strip()

#invocamos startswith() devuelve valores boleanos 
#necesita que la mayuscula tambien coincida
print cosa.startswith('hola')

#invocamos lower() se pasa a minusculas 
print cosa.lower()

#podemos unir lower() con startswith()
print cosa.lower().startswith('hola')
"""


#ejercicio 
#cuenta el numero de veces en una cadena usando count()
"""
cadena = ' Hola como te va, espero que todo este muy bien '
print cadena.count('o')
"""

#analisis de cadenas

#From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008
#extraer sola la segunda mitad
# uct.ac.za
#buscamos posiciones y luego rabanamos 
"""
datos = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
pos_arroba = datos.find('@')#posicion 
print pos_arroba

pos_esp = datos.find(' ',pos_arroba)#posicion de espacio despues de @
print pos_esp

host = datos[pos_arroba+1:pos_esp]
print host
"""


#operador formato 
#% es el de modulo pero cuando el primer operador es una cadena es formato 
#permite construir cadenas reemplazando partes de esas cadenas con los datos almacenados en variables
# %d significa que el segundo operador debe ser formateado como un entero ( d es decimal)

camellos = 42.025
print '%d' % camellos
print 'he divisado %d camellos ' % camellos

# %g formatear en punto flotante
print 'he divisado %g camellos ' % camellos 

# %s formatear una cadena
#el numerdo de elementos de la tupla debe coincidir con el numero de secuecias del formato
print 'en %d dias he visto %g %s' % (3, 0.1, 'gatos')
#salida : en 3 dias he visto 0.1 gatos

