# Definir una función generar_n_caracteres() que tome un entero n y un caracter,
# y devuelva el caracter multiplicado por n.


def generar_n_caracteres(n, c):
    res = ''
    for i in range(n):
        res += c[0]
    return res


assert generar_n_caracteres(5, 'x') == 'xxxxx', generar_n_caracteres(5, 'x')
assert generar_n_caracteres(1, 'e') == 'e', generar_n_caracteres(1, 'e')
assert generar_n_caracteres(0, 'e') == '', generar_n_caracteres(0, '')
assert generar_n_caracteres(8, 'a') == 'aaaaaaaa', generar_n_caracteres(8, 'aaaaaaaa')
