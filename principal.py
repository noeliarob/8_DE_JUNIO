import partida
import tiro
import tablero

jugadores = tablero.jugadores
puntajeParcial = tablero.puntajeParcial
cantidad = tablero.ingresoCantidadJug()
tablero.ingresoNombres(cantidad)
tablero.insertarColumnas(cantidad)

partida.iniciar_partida()

for turno in range(0,2):#El 2 hay que cambiarlo por 11, que es la cantidad de turnos por jugador. Puse 2 para no probar los 11 turnos.
    print("\n* Turno número", str(turno + 1)+" *\n")
    for a in range(0,cantidad):
        print("Debe tirar el jugador Número",(a + 1),":",(jugadores[a]))#Entre esta función y la siguiente hay que agregar la tirada random y lo de jugadas especiales.
        desglosar=tiro.programa_principal()
        puntos=desglosar[0]
        categoria=desglosar[1]
        tablero.anotacion(a+1,categoria,puntos)#Una vez que tenemos la jugada final y la detección de jugada especial se invoca a esta función para anotar.
        # Hay que cambiarle la función donde el usuario ingresa los valores por una función que los agregue automaticamente al detectarlos.
        # O en su defecto, hay que agregar una función que valide si los datos ingresados son correctos.
        tiro.dados.clear()
        tiro.contadorTiradas=1
        print("")
    print("* Resultados Parciales *\n")
    tablero.mostrarPuntajeParcial()# Luego de ingresar cada anotación se muestran los resultados parciales.

tablero.sumaPuntajeFinal(cantidad,puntajeParcial) #Esto solo se pone al final sino va a saltar error.
tablero.mostrarGanador(puntajeParcial,cantidad,jugadores) # Muestra que jugador ganó y con cuántos puntos
