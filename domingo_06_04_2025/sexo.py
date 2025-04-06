# Objetivo:
# Nombres: Robert Alexander Barrientos Palomino  
# Fecha : 06/04/2025

#===============================================
# Ingresa un género (M/F/O):
#
# Usted es Másculino
#
#
#===============================================

while True:
    genero_ingresado = str(input('Ingrese un género: ')).upper()
    if genero_ingresado == 'M' or genero_ingresado == 'F' or genero_ingresado == 'O':
        break
    print('Error de usuario ... Ingrese un género (M/F/O)')

if genero_ingresado == 'M':
    print('UD. es masculino')
elif genero_ingresado == 'F':
    print('UD. es femenina')
else:
    print('UD. no define su género')
