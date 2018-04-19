# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime


class Persona:
    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        fecha_hoy = datetime.datetime.now()
        e = fecha_hoy.year - self.nacimiento.year
        if fecha_hoy.month < self.nacimiento.month:
            e -= 1
        elif fecha_hoy.month == self.nacimiento.month and fecha_hoy.day < self.nacimiento.day:
            e -= 1
        return e


p = Persona(datetime.date(1993, 4, 20))
print(p.edad())
