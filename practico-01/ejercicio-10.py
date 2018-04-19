# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga


def mas_larga(palabras):
    larga = ''
    for p in palabras:
        if len(p) > len(larga):
            larga = p
    return larga


assert mas_larga(['hola', 'mundo', 'cadena', 'palabra']) == 'palabra'
assert mas_larga(['palabra', 'mundo', 'cadena', 'a']) == 'palabra'
assert mas_larga(['']) == ''
assert mas_larga(['hola']) == 'hola'
assert mas_larga(['hola', 'cadena', 'a']) == 'cadena'
