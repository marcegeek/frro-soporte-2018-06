# Programe una funcion que determine si un numero entero suministrado como argumento es primo

import math


def es_primo(n):
    if n < 0:
        n = -n
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # probando de 2 a sqrt(n)
        if n % i == 0:
            return False
    return True


assert not es_primo(0)
assert not es_primo(1)
assert es_primo(2)
assert es_primo(3)
assert not es_primo(-1)
assert es_primo(-2)
assert es_primo(-3)
assert not es_primo(8)
assert not es_primo(12191)
assert es_primo(1219177)
assert not es_primo(145151)
assert es_primo(1011013)
assert not es_primo(10110133)
assert es_primo(101101331)
