#Objetivo:  Uso de do - While(mientras)
#Nombre: Barrientos Palomino Robert
#Fecha: 05/04/2025

while True:
    letra = str(input('Usuario ingresar una OPCIÓN: '))
    convertir_letra = letra.upper()
    if convertir_letra =="A" or convertir_letra =="B" or convertir_letra =="C":
        break
    print('ERROR DE USUARIO ..... Ingresar una opción (A/B/C)!!!!')
print("OK saliste del bucle")