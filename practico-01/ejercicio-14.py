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


def laberinto_mostrable(lab, entrada, salida):
    val, err = validar_laberinto(lab, entrada, salida)
    if not val:
        raise ValueError(err)
    mostrable = []
    for fila in lab:
        mostrable.append([])
        for col in fila:
            if col:
                mostrable[-1].append(0)
            else:
                mostrable[-1].append(1)
    mostrable[entrada[0]][entrada[1]] = 2
    mostrable[salida[0]][salida[1]] = 3
    return mostrable


def mostrar_laberinto(mostrable, entrada, salida):
    filas = len(mostrable)
    columnas = len(mostrable[0])
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
            print(dicc[mostrable[i][j]], end='')
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


def alcanzables(lab, punto, visitados):
    filas = len(lab)
    columnas = len(lab[0])
    i, j = punto
    lista = []
    if i - 1 >= 0 and not lab[i - 1][j]:
        lista.append((i - 1, j))
    if i + 1 < filas and not lab[i + 1][j]:
        lista.append((i + 1, j))
    if j - 1 >= 0 and not lab[i][j - 1]:
        lista.append((i, j - 1))
    if j + 1 < columnas and not lab[i][j + 1]:
        lista.append((i, j + 1))
    for p in visitados:
        if p in lista:
            lista.remove(p)
    return lista


def buscar_salida(lab, entrada, salida):
    val, err = validar_laberinto(lab, entrada, salida)
    if not val:
        raise ValueError(err)
    visitar = [entrada]
    visitados = [entrada]
    rutas = [[entrada]]
    while 1:
        visitar_nuevo = []
        if salida in visitar:
            mostrable = laberinto_mostrable(lab, entrada, salida)
            for r in rutas:
                if salida in r:
                    for p in r:
                        mostrable[p[0]][p[1]] = 4
            return True, mostrable
        for nodo in visitar:
            al = alcanzables(lab, nodo, visitados)
            for e in al:
                visitar_nuevo.append(e)
                visitados.append(e)
                for i in range(len(rutas)):
                    for j in range(len(rutas[i])):
                        if rutas[i][j] == nodo:
                            rutas.append(rutas[i][:j + 1])
                            rutas[-1].append(e)
        visitar = visitar_nuevo
        if len(visitar) == 0:
            break
    return False, []


def correr(lab, entrada, salida):
    print('Laberinto:')
    mostrable = laberinto_mostrable(lab, entrada, salida)
    mostrar_laberinto(mostrable, entrada, salida)
    resuelve, mostrable = buscar_salida(laberinto, entrada, salida)
    if resuelve:
        print('Laberinto tiene solución:')
        mostrar_laberinto(mostrable, entrada, salida)
    else:
        print('Laberinto NO tiene solución')


laberinto = [[1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]]
entrada, salida = (2, 0), (5, 9)
correr(laberinto, entrada, salida)
laberinto = [[1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]]
correr(laberinto, entrada, salida)
salida = (1, 9)
correr(laberinto, entrada, salida)
