# Búsqueda de salida en un laberinto
# El laberinto se codifica como una matriz booleana de m filas por n columnas
# Las celdas con valor True son obstáculos mientras que las celdas con valor
# False son celdas por las que se puede caminar
# Hay un único punto de entrada al laberinto y otro único de salida.

# La matriz del laberinto es una lista de listas con valores booleanos:
# lab[i][j] es el valor de la celda en la fila i, columna j
# Los puntos de entrada y salida se codifican como tuplas de 2 elementos:
# (i, j) representa la posición de la celda correspondiente


def validar_laberinto(lab, entrada, salida):
    for fila in lab:
        if len(fila) != len(lab[0]):
            return False, 'hay columnas de ancho distinto'
    e_i, e_j = entrada
    s_i, s_j = salida
    if e_i < 0 or e_i >= len(lab) or e_j < 0 or e_j >= len(lab[0]):
        return False, 'punto de entrada fuera de rango'
    elif s_i < 0 or s_i >= len(lab) or s_j < 0 or s_j >= len(lab[0]):
        return False, 'punto de salida fuera de rango'
    if e_i != 0 and e_i != len(lab) - 1 and e_j != 0 and e_j != len(lab[0]) - 1:
        return False, 'punto de entrada fuera del borde del laberinto'
    if s_i != 0 and s_i != len(lab) - 1 and s_j != 0 and s_j != len(lab[0]) - 1:
        return False, 'punto de salida fuera del borde del laberinto'
    if entrada == salida:
        return False, 'punto de entrada y salida iguales'
    return True, ''


def transformar_laberinto(lab, entrada, salida):
    val, err = validar_laberinto(lab, entrada, salida)
    if not val:
        raise ValueError(err)
    matriz = []
    for fila in lab:
        matriz.append([])
        for col in fila:
            if col:
                matriz[-1].append(0)
            else:
                matriz[-1].append(1)
    matriz[entrada[0]][entrada[1]] = 2
    matriz[salida[0]][salida[1]] = 3
    return matriz


def mostrar_laberinto(lab, entrada, salida):
    matriz = transformar_laberinto(lab, entrada, salida)
    filas = len(matriz)
    columnas = len(matriz[0])
    print('┌', end='')
    for j in range(columnas):
        if (0, j) not in (entrada, salida):
            print('─', end='')
        else:
            print(' ', end='')
    print('┐')
    for i in range(filas):
        if (i, 0) not in (entrada, salida):
            print('│', end='')
        else:
            print(' ', end='')
        for j in range(columnas):
            dicc = {0: 'x', 1: '·',
                    2: '+', 3: '-',
                    4: '*'}
            print(dicc[matriz[i][j]], end='')
        if (i, columnas - 1) not in (entrada, salida):
            print('│')
        else:
            print()
    print('└', end='')
    for j in range(columnas):
        if (filas - 1, j) not in (entrada, salida):
            print('─', end='')
        else:
            print(' ', end='')
    print('┘')


laberinto = [[1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]]
mostrar_laberinto(laberinto, (2, 0), (1, 9))
