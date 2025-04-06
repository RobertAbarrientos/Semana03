# Objetivo; Realizar un programa que te solicite solo el ingreso de un número mayot a 10 y menor a 50
            #Y que imrprima si es un numero PAR o Impar, utiliza MOD.
# Nombres: Robert Alexander Barrientos Palomino  
# Fecha : 06/04/2025

#===============================================
# Ingresaa un número mayot a 10 y menor que 50:
#
# El número es par
#
#
#===============================================

while True:
    numero_ingresado = int(input('Ingree un número mayor a 10 y menor a 50: '))
    if numero_ingresado > 10 and numero_ingresado < 50:
        break
    else:
        print('ERROR DE USUARIO ... Ingree un número mayor a 10 y menor a 50')
if numero_ingresado % 2 == 0:
    print('El numero ingresado es par')
else:
    print('El numero ingresado es impar')