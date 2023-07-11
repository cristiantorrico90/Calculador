# -*- coding: utf-8 -*-


bandera = True
  # se crea una lista vacia para guardar los restos
lista = []
decimal = input("Ingrese un numero: ")
  # creamos la bandera para que fuerce alta la ultima division del decimal
while bandera == True:
    resto = decimal % 8
    decimal = decimal // 8 
    lista.append(resto)
    if decimal == 0:
        bandera = False
  # Coloca los elementos en reversa para concatenar de forma correcta la representacion numerica        
lista.reverse()
cadena = ""
  # para la variable cadena el for concatena los elementos convirtiendolos en String
for i in lista:
    cadena = cadena + str(i)
print cadena
