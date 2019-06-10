# base_datos
#algunas funciones de base de datos

import tablero_laura
import sqlite3
from datetime import datetime
base=sqlite3.connect('C://Noelia_base//Base_datos.db')
c=base.cursor()

#me pregunta el nombre de los jugadores y los guarda en la base de datos
def guardar_jugadores(jugadores):
    for i in jugadores:
        c.execute('insert into JUGADORES (NOMBRES) values ("{}");'.format(i))
    base.commit()

#me pregunta el nombre de la partida y lo guarda en la base de datos, al igual que la fecha y hora del momento que se creo.
def guardar_partida(nombre_partida):
    fecha = datetime.now()
    c.execute('insert into PARTIDA (NOMBRES,FECHA_HORA) values ("{}","{}");'.format(nombre_partida,fecha))
    base.commit()

###consultar primero el id de la partida segun el nombre

######UNIR TODAS LAS DE RESULTADOS PARCIALES EN UNA SOLA FUNCION:
###NECESITO QUE UNA VEZ QUE EL JUGADOR TIRO Y SE QUEDO CON LOS DADOS: ME QUEDE EN UNA LISTA LA CANTIDAD DE PUNTAJE QUE OBTUVO
###EN ESA JUGADA: EJEMPLO:
###1 2 3 4 5 6 E F P G 2G
##[0,0,0,8,0,0,0,0,0,0,0]

def guardar_resultados(resultados_parciales):
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS("1","2","3","4","5","6",E,F,P,G,"2G") values ({},{},{},{},{},{},{},{},{},{},{});'.format(resultados_parciales[0],resultados_parciales[1],resultados_parciales[2],resultados_parciales[3],resultados_parciales[4],resultados_parciales[5],resultados_parciales[6],resultados_parciales[7],resultados_parciales[8],resultados_parciales[9],resultados_parciales[10]))
    base.commit()


###UNIR TODAS LAS DE RESULTADOS PARCIALES EN UNA SOLA FUNCION:
#TENGO QUE UTILIZAR LA ULTIMA LISTA DE DADOS CON LA QUE SE QUEDO EL JUGADOR.
def guardar_dados(dados):
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS(d1,d2,d3,d4,d5) values ({},{},{},{},{});'.format(dados[0],dados[1],dados[2],dados[3],dados[4]))
    base.commit()

#------FUNCION QUE VALIDA:
#esta funcion la voy a usar al momento de crear la partida:
#Pido que me seleccione el id de la partida la cual ingrese el nombre
#si no existe la partida con el nombre que ingrese debe retornar false, y si existe me da el ID.
#cuando ingreso un nombre de partida, valido si ya existe una con ese nombre. Esta funcion deberia usarla para no crear dos partidas
#con el mismo nombre.
####------------- ACLARACION -----------####
######CUANDO HAGO UN SELECT UTILIZO fetchall:
######c.execute('select * from JUGADORES')
######r = c.fetchall()
#print(r)
def existe_partida(nombre_partida):
    query='SELECT ID FROM PARTIDA WHERE NOMBRE="{}" LIMIT 1'.format(nombre_partida)
    c.execute(query)
    partida=c.fetchall()
    if not partida:
        return False
    else:
        return partida[0][0]

##### FUNCION PARA CREAR PARTIDA:
### si no existe el nombre de la partida me va a crear una con ese nombre:
#CAMBIARLE NOMBRE:
def no_existe_partida(nombre_partida):
    existe = buscar_partida(nombre_partida)
    if not existe:
        guardar_partida(nombre_partida)
    else:
        print(existe)

#### ACA ESTOY SIMULANDO CREANDO LAS FUNCIONES:
jugadores=tablero_laura.jugadores
#guardar_jugadores(jugadores)

nombre_partida=input("ingrese nombre de la partida")
#guardar_partida(nombre_partida)

resultados_parciales=[0,0,0,12,0,0,0,0,0,0,0]
dados=[1,2,3,4,5]

guardar_resultados(resultados_parciales)

guardar_dados(dados)
