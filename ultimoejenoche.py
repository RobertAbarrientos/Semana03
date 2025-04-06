#Objetivo:  Uso de todo loaprendido:
# 1.- Validar el ingreso de un numero de 2 a 4 (enteros)
# 2.- Validar el ingreso de con la opcion A
# 3.- Con el número ingresado en el punto 1, realizar las iteracciones en un while
# 4-Imprime la multiplicacion acumulada
#Nombre: Barrientos Palomino Robert
#Fecha: 05/04/2025

# 1.- Validar el ingreso de un numero de 2 a 4 (enteros)
while True:
    numero = int(input('Ingresa un número de 2 a 4: '))
    if 2 <= numero <= 4:
        print('Número válido')
        break
    else:
        print('Número inválido, intenta nuevamente')

# 2.- Validar el ingreso de con la opcion A
while True:
    opcion = input('Ingrese la opción A: ').upper()
    if opcion == 'A':
        print('Opción válida')
        break
    else:
        print('Opción inválida, intenta nuevamente')

# 3.- Con el número ingresado en el punto 1, realizar las iteracciones en un while
i = 1
multiplicacion = 1
while i <= 5:
    valor = int(input("Ingrese el número: "))
    multiplicacion *= valor
    i+=1

# 4-Imprime la multiplicacion acumulada
    print("La multiplicación acumulada es: ", multiplicacion )
        