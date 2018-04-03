def longitud(lista):
    long = 0
    for i in lista:
        long += 1
    return long


cadena = 'cadena de prueba'
print('Longitud \'' + cadena + '\':', longitud(cadena))
cadena = 'probando'
print('Longitud de \'' + cadena + '\':', longitud(cadena))
print('Longitud de \'😀\':', longitud('😀'))  # esto en Python 3 da 1, no así en Python 2
lista = ['una cadena', 'otra cadena', 58, 0.5]
print('La lista:', lista, 'tiene', longitud(lista), 'elementos')
