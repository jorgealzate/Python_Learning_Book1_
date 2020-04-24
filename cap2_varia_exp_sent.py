"""
palabras reservadas en python

and del from not while
as elif global or with
assert else if pass yield
break except import print
class exec in raise
continue finally is return
def for lambda try

"""

#salida 4
print 4

#salida que tipo es 
#todo aquello en comillas es cadena 
print type ('hola mundo ')
#salida es:
# <type 'str'> 
# si solo usas type ('hola mundo ') en consola no se necesita el print
print type(17)
#salida es:
# <type 'int'> 
print type(3.20)
#salida es:
# <type 'float'> 

#variables
n = 17
print n
#las variables no pueden comenzar con numeros
#es buena constumbre empezar con letras minusculas
#el (_) guien bajo se puede usar para separar palabras
# el guion bajo se puede usar en el comienzo pero es mas usado 
#para librerias


#sentencias 
#una sentencia es una unidad de codigo que python puede ejecutar
#un script contiene un numero de sentencias 
print 1
x = 2
print x


#operadores
# + es suma 
# - es resta
# % es modulo
# * es multiplicacion
# / es division. // es division de enteros en python 3
# ** es exponenciacion
print 5**2
# 'x' + 'x' concatenacion

#expresiones
#es una combinacion de valores , variables y operadores
#si escribes una expresion en modo iterativo 
#el interprete la evalua y muestra el resultado
# >>> 1 + 1
# 2

#orden de opercaiones 
#cuando aparede mas de un operador el orden de evaluacion 
# depende de las reglas de precedencia.
#para los operadores matematicos Python sigue las convenciones matematicas
# el acronimo PEMDSR resutal util para recordar sus reglas 
#Asi que 2*3-1 es 5, no 4, y 6+4/2 es 8, no 5.

#concatenacion
p = '10'
q = '10'
print p + q 
#salida: 1010
 
#peticion de informacion del usuario 
"""
entrada = raw_input(' ingrese ejemplo :')
print entrada
"""
#La secuencia \n al final del mensaje representa un newline,
"""
entrada = raw_input('como te llamas ? \n')
print 'hola', entrada
"""

#si espera a que el usuario escriba un entero se debe convertir 
"""
x = int( raw_input(' ingrese numero '))
print x
"""




