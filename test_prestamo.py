import prestamo
import unittest
from unittest import TestCase


class TestPrestamo(TestCase):
    def test_valor_total_escenario_1(self):
        p = Prestamo()
        self.assertEqual(p.valor_total(2000, 2), 2080.8, "Se tiene exitosamente el escenario 1")

    def test_valor_total_escenario_2(self):
        p = Prestamo()
        self.assertEqual(p.valor_total(22000, 6),
                         None,
                         "Se tiene exitosamente el escenario 2")
    def test_valor_total_escenario_3(self):
        p = Prestamo()
        self.assertAlmostEqual(p.valor_total(5000, 4), 5407.5)

    def test_valor_total_escenario_4(self):
        p = Prestamo()
        self.assertAlmostEqual(p.valor_total(8000, 6), 8858)

    def test_valor_total_escenario_5(self):
        p = Prestamo()
        self.assertEqual(p.valor_total(8000, 7), None,
                                  "No se puede prestar 8000 a 7 meses")

    def test_valor_total_escenario_6(self):
        p = Prestamo()
        self.assertAlmostEqual(p.valor_total(10000, 10), 11960)

    def test_valor_total_escenario_7(self):
        p = Prestamo()
        self.assertEqual(p.valor_total(10000, 13), None,
                               "No se puede prestar 10000 a 13 meses")

    def test_valor_total_escenario_8(self):
        p = Prestamo()
        self.assertEqual(p.valor_total(2000, 6), None,
                                  "No se puede prestar 2000 a 6 meses maximo a 3")

if __name__ is "__main__":
    unittest.main()