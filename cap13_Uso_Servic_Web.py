#existen dos formatos para el intercambio de datos a traves
# de la web: el eXtensible Markup Language(lenguaje extensible de marcas)
# o XML --para intercambiar datos del tipo documento 
#JavaScript object notacion( notacion de objetos java script)
#0 JSON --para los programas quieren interambiar unos con otros diccionarios
#listas o informacion interna

"""
#aplicacion sencilla que analiza xml
import xml.etree.ElementTree as ET 
datos = '''
<persona>
    <nombre>Chuck</nombre>
    <telefono tipo="intl">
        +1 734 303 4456
    </telefono>
    <email oculto="si"/>
</persona>'''
arbol = ET.fromstring(datos)
print 'Nombre: ', arbol.find('nombre').text
print 'Attr: ', arbol.find('email').get('oculto')



#desplazamiento a traves de los nodos
#XML tiene muchos nodos y se escribe un bucle para procesarlos todos 
import xml.etree.ElementTree as ET
entrada = '''
<cosas>
    <usuarios>
        <usuario x="2">
            <id>001</id>
            <nombre>Chuck</nombre>
        </usuario>
        <usuario x="7">
            <id>009</id>
            <nombre>Brent</nombre>
        </usuario>
    </usuarios>
</cosas>'''
cosas = ET.fromstring(entrada)
lst = cosas.findall('usuarios/usuario')
print 'cantidad de usuarios: ', len(lst)
for elemento in lst:
    print 'Nombre ', elemento.find('nombre').text
    print 'Id ',elemento.find('id').text
    print 'Atributo ', elemento.get('x')



#javaScript Object Notacion - JSON
#el formato JSON es casi identico a la combinacion de listas y diccionarios de python
#por que python se invento antes que javaScrip
import json
entrada = '''
[
    { "id" : "001",
        "x" : "2",
        "nombre" : "Chuck"
    } ,
    { "id" : "009",
        "x" : "7",
        "nombre" : "Brent"
    }
]'''
info  = json.loads(entrada)
print 'cantidad de usuarios: ', len(info)
for elemento in info:
    print 'Nombre: ', elemento['nombre']
    print 'Id: ', elemento['id']
    print 'Atributo: ', elemento['x']
"""

#interface de programacion de aplicaciones
#definir y documentar contratos entre aplicaciones
#Application Program Interface o APIs
#un programa crea un conjunto de servicios disponibles
#para que lo usen otras aplicaciones y publica las APIS
#es decir las reglas que deben ser seguidas para 
#acceder a los servicios proporcionados por el programa
#construir programas con funcionalidades que incluyen el 
#acceso a servicios proporcionados por otros , se utiliza
#un planteamiento llamado :
#Arquitectura Orientada a Servicios o SOA
#SOA es aquel en el cual nuestra aplicacion principal
#usa los servicios de otras aplicaciones independiente que 
#contiene ella misma todo el codigo necesario para su implementacion
#ventajas:
#1 siempre se mantiene unica copia de datos
#2 los propietarios de los datos pueden imponer las reglas acerca 
#del uso de datos.

#servicio Geolocalizacion de Google
#pide una cadena de busqueda , llama a la API de geolocalizacion de google 
#y extrae informacion de JSON que nos devuelve

"""
import urllib
import json
urlservicio = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    direccion = raw_input('Introduzca ubicacion: ')
    if len(direccion) < 1 :break
    url = urlservicio + urllib.urlencode({'sensor':'false','address':'direccion'})
    print 'Recuperando: ', url
    uh = urllib.urlopen(url)
    datos = uh.read()
    print 'Recibidos',len(datos),'caracteres'

    try: 
        js = json.loads(str(datos))
    except: 
        js = None
    
    if 'status' not in js or js['status'] != 'OK':
        print '==== Fallo de Recuperacion ===='
        print datos
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    ubicacion = js['results'][0]['formatted_address']
    print ubicacion
"""












































