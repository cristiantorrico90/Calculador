  # -*- coding: utf-8 -*-

  # desde determinados archivos importamos las funciones de dichos archivos para invocarlo en este menu según la opcion elegida 
from dec_bin import decBin
from dec_rom import decRom 
from dec_hex import decHex
from dec_oct import decOct

print ("****Bienvenidos****")
print ("Seleccione una de las siguientes opciones a operar: ")
print ("1 para pasar de Decimal a Binarios// ")
print ("2 para pasar de Decimal a Romanos// ")
print ("3 para pasar de Decimal a Hexadecimal// ")
print ("4 para pasar de Decimal a Octal// ")
print ("Si no desea operar presione 5.")
menu = int(input("Ingrese la opción elegida: "))
while menu != 5:
    if menu == 1:
        print ("Usted ha elegido la opción de Decimal a Binarios")
        decimal = int(input("Ingrese un número entero para trasformar a números Binarios: "))
        resultado = decBin(decimal)
        print (resultado)
        menu = int(input("Ingrese nuevamente una opción para operar o la opcion 5 para salir: "))
  
    elif menu == 2:
        print ("Usted ha elegido la opcion de Decimal a Romanos")
        decimal = int(input("Ingrese un numero entero para transformar a números Romanos: "))
        resultado = decRom(decimal)
        print (resultado)
        menu = int(input("Ingrese nuevamente una opcion para operar o la opción 5 para salir: "))
    
    elif menu == 3:
        print ("Usted ha elegido la opción de Decimal a Hexadecimal")
        decimal = int(input("Ingrese un número entero para transformar a números Hexadecimales: "))
        resultado = decHex(decimal)
        print (resultado)
        menu = int(input("Ingrese nuevamente una opción para operar o la opción 5 para salir: "))
        
    elif menu == 4:
        print ("Usted ha elegido la opción de Decimal a Octal")
        decimal = int(input("Ingrese un número entero para transformar a números Octales: "))
        resultado = decOct(decimal)
        print (resultado)
        menu = int(input("Ingrese nuevamente una opción para operar o la opción 5 para salir: "))
    
    else:
        print ("Usted ha elegido una opción invalida.")
        menu = int(input("Ingrese un número para operar o 5 para salir: "))
else:
    print ("****Muchas gracias por utilizar el sistema de conversión****")