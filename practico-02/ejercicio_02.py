# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math


class Circulo:

    def __init__(self, radio):
        if radio <= 0.0:
            raise ValueError('radio <= 0')
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2.0 * math.pi * self.radio


if __name__ == '__main__':
    circ = Circulo(2.0)
    assert circ.perimetro() == 12.566370614359172
    assert circ.area() == 12.566370614359172
    circ = Circulo(4.0)
    assert circ.perimetro() == 25.132741228718345
    assert circ.area() == 50.26548245743669
