# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # valida regla
        valido = Socio(dni=12345679, nombre='Juan', apellido='García')
        self.assertTrue(self.ns.regla_1(valido))

        # DNI repetido
        invalido = socio
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor o igual a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Jua', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='María Fernanda', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor o igual a 15 caracteres
        invalido = Socio(dni=12345678, nombre='María Fernandaa', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Adrián', apellido='Suar')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor o igual a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Adrián', apellido='Sua')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Carlos', apellido='Ibarguengoitia')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor o igual a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Carlos', apellido='Ibarguengoitiaa')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        for i in range(12345678, 12345878):  # 200 socios
            socio = Socio(dni=i, nombre='Juan', apellido='Perez')
            self.ns.alta(socio)

        # post-condiciones:
        self.assertEqual(len(self.ns.todos()), 200)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio2 = Socio(dni=12345679, nombre='Juan', apellido='García')
        socio3 = Socio(dni=12345680, nombre='Roberto', apellido='Rodríguez')
        self.ns.alta(socio1)
        self.ns.alta(socio2)
        self.ns.alta(socio3)
        exito = self.ns.baja(socio2.id)

        # post-condiciones:
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 2)

    def test_buscar(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio2 = Socio(dni=12345679, nombre='Juan', apellido='García')
        socio3 = Socio(dni=12345680, nombre='Roberto', apellido='Rodríguez')
        self.ns.alta(socio1)
        self.ns.alta(socio2)
        self.ns.alta(socio3)
        encontrado = self.ns.buscar(socio2.id)

        # post-condiciones: encuentra el socio 2
        self.assertEqual(encontrado, socio2)

    def test_buscar_dni(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio2 = Socio(dni=12345679, nombre='Juan', apellido='García')
        socio3 = Socio(dni=12345680, nombre='Roberto', apellido='Rodríguez')
        self.ns.alta(socio1)
        self.ns.alta(socio2)
        self.ns.alta(socio3)
        encontrado = self.ns.buscar_dni(socio2.dni)

        # post-condiciones: encuentra el socio 2
        self.assertEqual(encontrado, socio2)

    def test_todos(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio2 = Socio(dni=12345679, nombre='Juan', apellido='García')
        socio3 = Socio(dni=12345680, nombre='Roberto', apellido='Rodríguez')
        self.ns.alta(socio1)
        self.ns.alta(socio2)
        self.ns.alta(socio3)

        # post-condiciones:
        self.assertEqual(len(self.ns.todos()), 3)

    def test_modificacion(self):
        pass
