#me pide un valor, y recorre cuantas veces esta ese valor dentro de la jugada
def SalidaDeNumero(dados,valor):
  cantidad_de_repeticiones=0
  for i in dados:
      if i==valor:
          cantidad_de_repeticiones+=1
  multiplicacion = (valor*cantidad_de_repeticiones)
  print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces. Obtuvo",multiplicacion,"puntos.")
  return multiplicacion

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 5 veces dentro de jugada, me retorna true
def EsGenerala(dados):
   for i in range (0,len(dados)):
      if dados.count(dados[i])==5:
          return True
      else:
          return False

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 4 veces dentro de jugada, me retorna true
def EsPoker(dados):
   for i in range (0,len(dados)):
      if dados.count(dados[i])==4:
          return True
      else:
          return False

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 3 veces dentro de jugada, me retorna true
#si hay otro valor que esta 2 veces me retorna true.
def esFull(dados):
    hay_tres=False
    hay_dos=False
    for i in range (0,len(dados)):
        if dados.count(dados[i])==3:
            hay_tres=True
        if dados.count(dados[i])==2:
           hay_dos=True
    return hay_tres and hay_dos

#la funcion establece las dos posibles escaleras que existen dentro del juego.
#luego ordena la jugada, si es igual a alguna de las dos escaleras retorna true.
def esEscalera(dados):
    esc1=[1,2,3,4,5]
    esc2=[2,3,4,5,6]
    if sorted(dados)==esc1 or sorted(dados)==esc2:
        return True
    else:
        return False
