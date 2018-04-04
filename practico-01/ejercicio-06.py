# Definir una función inversa() que calcule la inversión de una cadena


def inversa(cadena):
    inv = ''
    for i in range(len(cadena) - 1, -1, -1):
        inv += cadena[i]
    return inv


assert inversa('estoy probando') == 'odnaborp yotse', inversa('estoy probando')
assert inversa('hola mundo') == 'odnum aloh', inversa('hola mundo')
assert inversa('un símbolo especial: 😀') == '😀 :laicepse olobmís nu', inversa('un símbolo especial: 😀')  # Python 3 maneja bien esto
