# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from datetime import datetime
from ejercicio_03 import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return int(self.cantidad_aprobadas/self.cantidad_materias * 100 + 0.5)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        anio_actual = datetime.now().year
        return self.edad - (anio_actual - self.anio)

    def print_data(self):
        super().print_data()
        print('Carrera: ' + self.carrera)
        print('Materias de la carrera:', self.cantidad_materias)
        print('Materias aprobadas:', self.cantidad_aprobadas)
        print('Porcentaje completado: {p} %'.format(p=self.avance()))
        print('Edad al ingreso: {e}'.format(e=self.edad_ingreso()))


if __name__ == '__main__':
    estu = Estudiante('Carlos', 26, 'M', 65.0, 1.6, 'ISI', 2010, 52, 20)
    estu.print_data()
    assert estu.avance() == 38
