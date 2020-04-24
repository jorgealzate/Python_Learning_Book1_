#Iteraciones

# x = x + 1
#antes de actualizar una variable se debe inicializar
# x = 0
# incrementar x = x + 1
#decrementar x = x -1 

#sentencia while
"""
n = 5
while n > 0:
    print n
    n = n - 1
print 'despegue'
"""


#bucles infinitos y break
#debes tener cuidado de hacer un bucle infinito si que su sentencia
#no permita pararlo 
#el tipico while True: 
#se usa break para pararlo

#termina hasta que se escriba de entrada 'fin'
#por favor probar por consola
#por IDE depronto se queda ya que se ingresa mas otros caracteres junto con 'fin'
"""
while True:
    linea = raw_input('> ')
    if linea == 'fin':
        break
    print linea
print 'Terminado'
"""


#finalizar iteraciones con continue
#estando en un bucle se necesita terminar con la iteracion actual
#y saltar a la siguiente de forma inmediata
#se usa la sentencia continue
#aqui si se escribe # salta sin mostrar nada 
#y termina si se escribe fin
"""
while True:
    linea = raw_input('> ')
    if linea[0] == '#':
        continue
    if linea == 'fin':
        break
    print linea
print 'Terminado'
"""


#bucles definidos usando for
#se repite a traves de un conjunto conocido de elementos
#ejecuta tantas iteraciones como elementos hay en el conjunto 
"""
amigos = ['jose', 'jorge', 'sally'] #lista
for amigo in amigos:
    print 'Feliz dia nuevo : ', amigo 
print 'Terminado'
"""

#diseno de bucles
#bucle de recuento y suma
"""
contador = 0 
for valor in [3, 41, 12, 9, 74, 15]:
    contador = contador + 1
print 'numero de elementos : ', contador
""" 

#calcula el total de un grupo de numeros 
"""
total = 0
for valor in [3, 41, 12, 9, 74, 15]:
    total = total + valor 
print 'Total es : ', total
"""

#usando funciones ya definidad
"""
import math
lts = [3, 41, 12, 9, 74, 15]
print 'cantidad elementos usando funcion: ',  len(lts)
print 'total suma usando funcion: ',  math.fsum(lts)
"""


#bucle para encontrar el mayor de una lista
"""
mayor = None 
print 'Antes: ', mayor
for valor in [3, 41, 12, 9, 74, 15]:
    if mayor is None or valor > mayor:
        mayor = valor 
    print 'Bucle: ', valor , mayor
print 'Mayor: ', mayor

#usando una funcion 
l = [3, 41, 12, 9, 74, 15]
print 'Mayor usando funcion : ', max(l)
"""

#bucle para calcular el mas pequeno
"""
menor = None 
print 'Antes: ', menor
for valor in [3, 41, 12, 9, 74, 15]:
    if menor is None or valor < menor:
        menor = valor 
    print 'Bucle: ',valor ,menor
print 'Menor: ' ,menor
#usando una funcions 
lm = [3, 41, 12, 9, 74, 15]
print 'menor usando funcion: ', min(lm)
"""

#depuracion 
#cuando el programa es muy extenso 
#lo mejor es usar depuracion por biseccion:
#se parte el problema a la mitad 
#anades una sentencia print y has funcionar el programa

#ejercicio 5.10
"""
print 'Termina con fin' 
valor = 0
cont = 0
while True:
    ent = raw_input('ingrese numero ')
    try:
        num = int(ent)
        valor = valor + num
        cont = cont + 1
    except: 
        if ent == 'fin':
            print '********RESULTADOS**********'     
            print 'valor total: ',valor
            print 'media : ', valor / 2
            print 'cantidad numeros : ',cont
            break
        else:
            print ' dato erroneo , continue ...'
"""

#ejercicio 5.2
print 'Termina con fin' 
valor = list()
while True:
    ent = raw_input('ingrese numero ')
    try:
        num = int(ent)
        valor.append(num)
    except:
        if ent == 'fin':
            print '*********RESULTADO*******'
            print 'maximo numero es :', max(valor)
            print 'minimo numero es :', min(valor)
            break
        else:
            print 'dato erroneo , continue...'



    





