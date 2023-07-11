  # -*- coding: utf-8 -*-

  # se asigna una bandera para ingresar a la iteracion de la divion del decimal
   
  
def decBin(decimal): 
    bandera = True
    lista = []
    #decimal = input("Ingrese un numero entero: ")
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
    print cadena
    
#decimal = int(input("Ingrese un numero entero: "))
#decBin(decimal)