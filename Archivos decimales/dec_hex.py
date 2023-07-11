# -*- coding: utf-8 -*-

  # creamos el diccionario con su clave y valor correspondiente
dec_hex = {0:"0",
           1:"1",
           2:"2",
           3:"3",
           4:"4",
           5:"5",
           6:"6",
           7:"7",
           8:"8",
           9:"9",
           10:"A",
           11:"B",
           12:"C",
           13:"D",
           14:"E",
           15:"F"}

bandera = True
  # creamos una lista vacia para agregar los resultados de los restos
lista = []
decimal = input("Ingrese un numero: ")
while bandera == True:
    resto = decimal % 16
    decimal = decimal // 16 
    lista.append(resto)
    if decimal == 0:
        bandera = False
  # Coloca los elementos en reversa para concatenar de forma correcta la representacion numerica        
lista.reverse()
  # creamos una nueva lista para agregar el valor convertido desde el diccionario
nueva_lista = []
  # lo que realiza este For es agregar a la lista nueva el valor asociado al indice del diccionario 
for indice in lista:
    nueva_lista.append(dec_hex[indice])
cadena = ""
  # para la variable cadena el for concatena los elementos de la lista nueva convirtiendolos en String
for indice in nueva_lista:
    cadena = cadena + str(indice)
print cadena
