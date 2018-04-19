# Programa que pide al usuario una lista de números e
# imprime en pantalla el máximo y mínimo de los números introducidos al final,
# cuando el usuario introduce “fin”
# Escribe ahora el programa de modo que almacene los números que el usuario introduzca
# en una lista y usa las funciones Max () y min () para calcular los números máximo y mínimo
# después de que el bucle termine

s = ''
numeros = []
while s != 'fin':
    s = input('Ingrese un nº entero (o fin para terminar) ')
    if s != 'fin':
        try:
            n = int(s)
            numeros.append(n)
        except ValueError:
            print('El valor ingresado debe ser un número entero (o fin para terminar)')
if len(numeros) != 0:
    print('Máximo:', max(numeros))
    print('Mínimo:', min(numeros))
else:
    print('No se ingresó ningún número')
