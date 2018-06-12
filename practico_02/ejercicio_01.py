# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        if base <= 0.0 or altura <= 0.0:
            raise ValueError('base y/o altura <= 0')
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


if __name__ == '__main__':
    rect = Rectangulo(5.0, 2.0)
    assert rect.area() == 10.0
    rect = Rectangulo(3.0, 8.0)
    assert rect.area() == 24.0
