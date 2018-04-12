# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False.


def es_vocal(letra):
    letra = letra.lower()
    return letra in ['a', 'e', 'i', 'o', 'u']


assert es_vocal('a')
assert es_vocal('A')
assert es_vocal('I')
assert not es_vocal('h')
assert not es_vocal('X')
