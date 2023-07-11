# -*- coding: utf-8 -*-


  #definimos una funcion con el nombre decOct y le asignamos como parametro los valores ingresados en decimal
def decOct(decimal): 
    bandera = True
      # se crea una lista vacia para guardar los restos como elementos
    lista = []
    
      # creamos la bandera para que fuerce hasta la ultima division del decimal
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
    return ("El resultado en números Octal es: " + cadena)
    


#decimal = input("Ingrese un numero: ")
#decOct(decimal)