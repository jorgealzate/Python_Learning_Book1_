#Funciones 


#funciones internas 
"""
#operan con cualquier conjunto de valores
print max( 'hola mundo ') #caracter mas grande
#salida u
print min( 'hola mundo ')#caracter mas pequeno
#salida ' '
print len(' hola mundo ')#cuantos caracteres hay 
#salida 12

#de conversion de tipo
print int('32')
#salida 32
#corta el numero flotante mas no redondea
print int(3.99999)
#salida 3
print float(32)
#salida 32.0
print str(32)#convierte el numero en cadena
#salida '32'
"""

#numeros aleatorios
#numeros seudoaleatorios casi parecidos a los aleatorios de verdad
#la funcion random devuelve numeros pseudoaleatorios flotantes entre 0.0 y 1.0 
#incluye el 0.0 pero no el 1.0
#tambien proporciona valores aleatorios de 
#distribuciones continuas, incluyendo gausiana, exponencial
#gamma y unas cuantas mas 
"""
import random
for i in range(10):
    x = random.random()#no es necesario un for
    print x

for k in range(10):
    y = random.randint(5,10)#no es necesario un for
    print y
#elige de la lista 
t= [1,2,3,4,5,6,7,8,9,10]
print random.choice(t)
"""

#funciones matematicas
"""
import math
int_senal = 10
int_ruido = 5
relacion = int_senal / int_ruido
decibelios = 10 * math.log10(relacion)
radianes = 0.7
altura = math.sin(radianes)
print altura
"""

#funciones nuevas
#para terminar la funciones debes poner una linea vacia
#las funciones deben ser ejecutadas antes que se llamen por primera vez
#cuando leeas un programa no simpres es de arriba hacia abajo
#tiene sentido hacerlo siguiendo el flujo de la ejecucion
"""
def muestra_estribillo():
    print 'soy un lenador, que alegria '
    print 'duermo toda la noche y trabajo todo el dia'

print muestra_estribillo()

#funciones que con parametros
def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

print suma(10,12)
print resta(22,15)

"""
def calculo_salario(horas, tarifa):
    return horas * tarifa

ent = raw_input('ingrese cant de horas : ')
try:
    horas_lab = float(ent)
    salario = 475.0
    precio_hora = salario / 40
    if horas_lab > 40:
        x = horas_lab - 40
        pago = calculo_salario(x,precio_hora*1.5)
        print 'pago es de : ',salario + pago
    else:
        print 'no tiene horas extras '
except:
    print 'por favor ingrese las horas '
