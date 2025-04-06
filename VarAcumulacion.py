#Objetivo:  Uso de variable de acumulacion}
#Nombre: Barrientos Palomino Robert
#Fecha: 05/04/2025

i = 0 
varAcumulacion = 0
while i <= 3:
    monto = int(input('Ingrese un monto: '))
    varAcumulacion =  varAcumulacion + monto
    i += 1

print("Acumulación es: ",varAcumulacion)