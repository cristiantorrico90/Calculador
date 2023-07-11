  # -*- coding: utf-8 -*-
  
  
  #definimos una funcion con el nombre decBin y le asignamos como parametro los valores ingresados en decimal
def decBin(decimal): 
  # se asigna una bandera para ingresar a la iteracion de la division del decimal
    bandera = True
  # creamos una lista vacia
    lista = []
    
    while bandera == True:
        resto = decimal % 2
        decimal = decimal // 2 
          # Se enlista los valores del resto como elementos
        lista.append(resto)
        if decimal == 0:
            bandera = False
      # Coloca los elementos en reversa para concatenar de forma correcta la representacion numerica        
    lista.reverse()
    cadena = ""
      # para la variable cadena el for concatena los elementos convirtiendolos en String
    for i in lista:
        cadena = cadena + str(i)
    return ("El resultado en números Binarios es: " + cadena)