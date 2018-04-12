# Definir una función es_palindromo() que reconoce palíndromos


def es_palindromo(str):
    for i in range(0, len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


assert es_palindromo('radar')
assert es_palindromo('reconocer')
assert not es_palindromo('banana')
assert es_palindromo('a')
assert es_palindromo('😀')
