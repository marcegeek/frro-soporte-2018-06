# Escribir una función multip() que multiplique respectivamente
# todos los números de una lista.


def multip(lista):
    res = 1
    if len(lista) == 0:
        return 0
    for n in lista:
        res *= n
    return res


assert(multip([1, 2, 3, 4]) == 24)
assert(multip([1, 2, 3]) == 6)
assert(multip([1, 2, 3, 5]) == 30)
assert(multip([0]) == 0)
assert(multip([]) == 0)
