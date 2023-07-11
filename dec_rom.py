  # -*- coding: utf-8 -*-
  
  
  #definimos una funcion con el nombre decRom y le asignamos como parametro los valores ingresados en decimal
def decRom(decimal): 
    
      # Creamos dos listas, una de numeros y otra de la representacion de los numeros en letras
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ["M", "CM", "C", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]   
    cadena = ""
    i = 0 
      # se crea un while que compara el decimal con los elementos de la lista  
    while decimal > 0:
        for _ in range (decimal // numeros[i]):
            cadena += letras[i]
            decimal -= numeros[i]
        i += 1
    return ("El resultado en número Romano es: " + cadena)