# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga


def mas_larga(palabras):
    larga = ''
    for p in palabras:
        if len(p) > len(larga):
            larga = p
    return larga


assert mas_larga(['hola', 'mundo', 'cadena', 'palabra']) == 'palabra', mas_larga(['hola', 'mundo', 'cadena', 'palabra'])
assert mas_larga(['palabra', 'mundo', 'cadena', 'a']) == 'palabra', mas_larga(['palabra', 'mundo', 'cadena', 'a'])
assert mas_larga(['']) == '', mas_larga([''])
assert mas_larga(['hola']) == 'hola', mas_larga(['hola'])
assert mas_larga(['hola', 'cadena', 'a']) == 'cadena', mas_larga(['hola', 'cadena', 'a'])
