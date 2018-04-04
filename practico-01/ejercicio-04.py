# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False.


def es_vocal(letra):
    letra = letra.lower()
    return letra in ['a', 'e', 'i', 'o', 'u']


print('es_vocal(\'a\'):', es_vocal('a'))
print('es_vocal(\'A\'):', es_vocal('A'))
print('es_vocal(\'I\'):', es_vocal('I'))
print('es_vocal(\'h\'):', es_vocal('h'))
print('es_vocal(\'X\'):', es_vocal('X'))
