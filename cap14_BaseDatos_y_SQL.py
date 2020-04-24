# CAPITULO 14 BASES DE DATOS Y SQL

"""
este libro esta centrado a SQLite
ya que es una base de datos muy habitual y ya viene 
integrada dentro de python.
SQLite esta disenada para ser incrustada dentro de otras
aplicaciones de modo que proporciones soporte para bases 
de datos de otras aplicaciones 
navegador Firefox usa SQLite internamente.
http://sqlite.org/
SQLite se usa para rastreo de twitter.
aqui lo que conocemos como tabla fila columna es igual 
a decir relacion , tupla y atributo.
Hay muchas operaciones que se pueden realizar de forma mas 
eficaz usando un add-on para firefox llamado:
SQLite Database Manager, se descarga en :
https://addons.mozilla.org/en-us/firefox/addon/sqlite-manager/
utilizando el navegador se puede crear tablas , insertar , y editar
datos o ejecutar consultas SQL
diferentes tipos de datos soportados en SQLite:
http://www.sqlite.org/datatypes.html

"""


#crear un archivo de base de datos llamado Canciones
#como es sencillo se almacena en el directorio 
#por lo que se hace conexion es por que habitualmente se 
#guarda en un servidor de base de datos 
#la llamada cursor() es parecida a la open() en textos
#los comando se expresan en lenguaje estandar :}
#SQL -lenguaje de consultas estructurado 
#Structure Query Language http://en.wikipedia.org/wiki/SQL

"""
import sqlite3

conn = sqlite3.connect('musica.sqlite3')
cur = conn.cursor()
#elimina la tabal canciones si existe
cur.execute('DROP TABLE IF EXISTS Canciones')
#crea una tabla llamada canciones con dos columnas
cur.execute('CREATE TABLE Canciones (titulo TEXT, reproducciones INTEGER)')

conn.close()
"""

#insertado datos a la base de datos 
import sqlite3

conn = sqlite3.connect('musica.sqlite3')
cur = conn.cursor()

cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?) ',('Thunderstruck', 20) )
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES ( ?, ? )', ( 'My Way', 15 ) )
conn.commit()

print 'Canciones'
cur.execute('SELECT titulo, reproducciones FROM Canciones')
for fila in cur:
    print fila

cur.execute('DELETE FROM Canciones WHERE reproducciones < 100')
conn.commit()

cur.close()

#salida:
#Canciones:
#(u'Thunderstruck', 20)
#(u'My Way', 15)
# que empiece con 'u' significa que es unicode
