  # -*- coding: utf-8 -*-



def decRom(decimal): 
    #decimal = int(input("Ingrese un numero: "))
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
    print cadena

#decimal = int(input("Ingrese un numero: "))
#decRom(decimal)