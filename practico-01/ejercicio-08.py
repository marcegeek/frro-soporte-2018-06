# Definir una función superposicion() que tome dos listas y devuelva True
# si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.


def superposicion(lista1, lista2):
    for e1 in lista1:
        for e2 in lista2:
            if e1 == e2:
                return True
    return False


assert superposicion(['a'], ['b', 'c', 'a'])
assert superposicion(['c'], ['b', 'c', 'a'])
assert superposicion(['b', 'c', 'a'], ['a'])
assert superposicion(['b', 'c', 'a'], ['c'])
assert not superposicion(['b', 'c', 'a'], ['h'])
assert not superposicion([], [])
