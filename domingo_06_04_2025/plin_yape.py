# Objetivo: Buscar género
# Nombres: Robert Alexander Barrientos Palomino  
# Fecha : 06/04/2025

while True:
    opcion = str(input('Ud. va a yapear o plinear (Y/P/E): ')).upper()
    if opcion in ['Y','P','E']:
        break
    else:
        print(' Opción inválida ... Ud. va a yapear o plinear (Y/P/E)')

while True:
    cantidad_deposito = float(input('Ingrese número mayor a 0: '))
    if cantidad_deposito > 0.00:
        break
    else: 
        print('ERROR DE USUARIO Ingrese número mayor 0 ')
i = 0
monto_acumulado = 0
while i < cantidad_deposito:
    monto = float(input(f"Ingrese un monto {i}: "))
    monto_acumulado += monto
    i += 1
if opcion == "Y":
    dscto_yape = monto_acumulado * 0.12
    total_yape = monto_acumulado - dscto_yape
    print(f"\tEl monto acumulado es: {monto_acumulado:.2f}")
    print(f"\tEl monto con descuento es : {total_yape:.2f}")
    
elif opcion == "P":
    dscto_plin = monto_acumulado * 0.13
    total_plin = monto_acumulado - dscto_plin
    print(f"\tEl monto acumulado es: {monto_acumulado:.2f}")
    print(f"\tEl monto con descuento es : {total_plin:.2f}")

elif opcion == "E":
    print(f"\tEl monto acumulado es: {monto_acumulado}")
    print(f"\tEl monto sin descuento es : {monto_acumulado}")

