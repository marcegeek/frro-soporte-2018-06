# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.


import random


class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.generar_dni()
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        return self.edad >= 18

    # llamarlo desde __init__
    def generar_dni(self):
        self.dni = random.randrange(10000000, 100000000)

    def print_data(self):
        print('Nombre: {nombre}'.format(nombre=self.nombre))
        print('Edad: {edad}'.format(edad=self.edad))
        print('Sexo: {sexo}'.format(sexo=self.sexo))
        print('Peso: {peso}'.format(peso=self.peso))
        print('Altura: {altura}'.format(altura=self.altura))
        print('DNI: {dni}'.format(dni=self.dni))


if __name__ == '__main__':
    p = Persona('Carlos', 42, 'M', 50.0, 1.6)
    p.print_data()
    assert p.es_mayor_edad()
    p.edad = 17
    assert not p.es_mayor_edad()
    p.edad = 18
    assert p.es_mayor_edad()
