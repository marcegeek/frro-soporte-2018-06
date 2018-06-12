# Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa por consola


def suma(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


try:
    n = int(input('Ingrese un número entero: '))
    print('La suma de los números de 1 a', n, 'es', suma(n))
except ValueError:
    print('El valor ingresado debe ser un número entero')
