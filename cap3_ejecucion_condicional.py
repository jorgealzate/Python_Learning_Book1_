#expresion booleana
#aquella que puede ser verdadera o falsa

print 5 == 5
#salida : True

print 5 == 6
#salida : False

print type(True)
#salida : <type 'bool'>

# x != y       x es distinto de y
# x > y        x es mayor que y
# x < y        x es menor que y 
# x >= y       x es mayor o igual que y
# x <= y       x es menor o igual que y
# x is y       x es lo mismo que y
# x is not y   x no es lo mismo que y 
# x == y       x es igual que y

#operadores logicos:
# and   es y
# or    es o
# not   es no
#x > 0 and x <10  es verdadero solo cuando x es mayor que 0 y menor que 10.
#n % 2 == 0 or n % 3 == 0

#cualquier numero distinto de 0 se interpreta como verdader
#>>> 17 and True
#salida : True


#ejecucion condicional
x = 8
y = 10

if x > 0: #condicion
    print 'es positivo: ', x #sentencias y va con un tabulado o 4 espacios

if x < 0:
    pass  # sentencia que no hace nada--usada para luego gestionar las sentencias 

#ejecucion alternativa 
if x%2 == 0:
    print 'x es par '
else :
    print 'x es impar '

#condiciones encadenadas
if x < y:
    print ' x es menor que y'
elif x > y:
    print 'x es mayor que y'
else:
    print 'x e y son iguales'

#no hay limite para elif 
# si hay clausula para la else pero no es obligatoria
choice = 'c'
if choice == 'a':
    print 'Respuesta incorrecta'
elif choice == 'b':
    print 'Respuesta correcta'
elif choice == 'c':
    print 'Casi, pero no es correcto'

#condiciones anidadas
if x == y:
    print 'x e y son iguales'
else:
    if x < y:
        print 'x es menor que y'
    else:
        print 'x es mayor que y'
#reescribamos este codigo con un unico condicional
if 0 < x:
    if x < 10:
        print 'x es un numero positivo con un solo digito'

#capturar excepciones usando try - except
"""
ent = raw_input('ingrese temperatura Fahrenheit: ')
try:
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0 /9.0
    print cel
except:
    print 'por favor , introduzca un numero'
"""


#cortocircuito
#se debe tener cuidado de que una variable valga 0
#asi en una expresion logica no genere error 
#si la variable vale 0 se debe corregir con otra expresion logica
"""
x = 1
y = 0 #la que vale 0
print x >= 2 and y != 0 and (x/y) > 2
"""

"""
entrada = raw_input('introduzca horas : ')
try:
    horas = int(entrada)
    tarifa_hora= 10
    salario = 475
    if horas > 40:
        pago = ((horas-40) * 1.5) + salario
        print 'pago por horas extras ' , pago
    else:
        print ' no tiene horas extras'
except:
    print 'por favor introduce un numero '
"""

"""
print 'ingrese puntuacion entre 0.0 a 1.0\n'
ent = raw_input('ingrese puntuacion : ')
try:
    puntuacion = float(ent)
    if puntuacion < 0.6:
        print 'Insuficiente'
    elif puntuacion >= 0.6 and puntuacion < 0.7:
        print 'Suficiente'
    elif puntuacion >= 0.7 and puntuacion < 0.8:
        print 'Bien'
    elif puntuacion >= 0.8 and puntuacion < 0.9:
        print 'Notable'
    elif puntuacion >= 0.9 and puntuacion <= 1.0:
        print 'Sobresaliente'
    elif puntacion > 1.0:
        print ' por favor ingrese puntuacion de 0.0 a 1.0'
except:
    print ' por favor ingrese puntuacion de 0.0 a 1.0'
"""