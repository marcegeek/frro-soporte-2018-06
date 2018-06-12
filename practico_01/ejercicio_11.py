# Determinar la cantidad de dígitos de un número ingresado

import math


def digitos(n):
    if n < 0:
        n *= -1
    if n != 0:
        return math.floor(math.log10(n)) + 1
    return 1


try:
    n = int(input('Ingrese un número entero: '))
    print('El número', n, 'tiene', digitos(n), 'dígitos')
except ValueError:
    print('El valor ingresado debe ser un número entero')
