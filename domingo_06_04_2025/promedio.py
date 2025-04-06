# Ud. va a ingresar una cantidad de notas(iteraciones)
# Deberá de validar el ingreo de la cantidad(DO WHILE)
# Validar el ingreso de cada nota (0-20) 
# Debera utilizar variablñes de incremento y acumulacion
# Debera de acumular las notas y promediarlas
# Resultado
# print('Usted ingreso n notas)
    #La suma de las notas es:
    #El promedio de las notas:


cantidad_notas = 0
while cantidad_notas <= 0:
    cantidad_notas = int(input("Cuantas notas tiene el alumno: "))

suma = 0

i = 1
while i <= cantidad_notas:
    nota = int(input(f"Ingrese nota {i}: "))
    if 0 <= nota <= 20:
        suma += nota
        i += 1
    else:
        print("La nota debe estar entre 0 y 20.")

promedio = suma / cantidad_notas

print("=====Resultado=====")
print(f"Ud. ingresó {cantidad_notas} notas")
print(f"La suma de las notas es: {suma}")
print(f"El promedio de las notas es: {promedio:.2f}")