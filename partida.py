import base_datos_avanzado

nombre_partida=''

def opcion_partida():
    global nombre_partida
    opcion=int(input("Ingrese una opcion:\n"
          "1-Nueva Partida\n"
          "2-Reanudar Partida"))
    if opcion==1:
        nombre_partida = input("Ingrese el nombre de la nueva partida:")
    elif opcion==2:
        nombre_partida = input("Ingrese el nombre de la partida que desea reanudar:")
    else:
        print("La opción seleccionada no es valida")
    return opcion

def iniciar_partida():
    continuar=True
    global nombre_partida
    opcion=opcion_partida()
    while continuar==True:
        if opcion==1:
            busqueda=base_datos_avanzado.buscar_partida(nombre_partida)
            if busqueda==False:
                return base_datos_avanzado.guardar_partida(nombre_partida)
            else:
                nombre_partida=input("El nombre de la partida ya existe. Por favor ingrese otro nombre:")
        elif opcion==2:
            return base_datos_avanzado.buscar_partida(nombre_partida)



iniciar_partida()

###def verificar_opcion():
#    if opcion_partida()==1:
#        base_datos_avanzado.buscar_partida(nombre_partida)
#        existe =base_datos_avanzado.ar_partida(nombre_partida)
#        if not existe:
#            guardar_partida(nombre_partida)
#        else:
#            print(existe)
#    elif opcion_partida()==2:
#        base_datos_avanzado.buscar_partida(nombre_partida)


