def longitud(lista):
    long = 0
    for i in lista:
        long += 1
    return long


cadena = 'cadena de prueba'
assert longitud(cadena) == 16
cadena = 'probando'
assert longitud(cadena) == 8
assert longitud('😀') == 1  # esto en Python 3 da 1, no así en Python 2
lista = ['una cadena', 'otra cadena', 58, 0.5]
assert longitud(lista) == 4
