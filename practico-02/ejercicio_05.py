# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    carreras = {}
    for e in estudiantes:
        if e.carrera not in carreras:
            carreras[e.carrera] = 1
        else:
            carreras.update({e.carrera: carreras[e.carrera] + 1})
    return carreras


if __name__ == '__main__':
    estudiantes = [Estudiante('Carlos', 23, 'M', 65.0, 1.6, 'ISI', 2010, 52, 20),
                   Estudiante('Roberto', 21, 'M', 68.0, 1.61, 'IQ', 2010, 48, 15),
                   Estudiante('José', 22, 'M', 70.0, 1.68, 'ISI', 2013, 52, 16)]
    assert organizar_estudiantes(estudiantes) == {'ISI': 2, 'IQ': 1}
