import unittest
import pytest
from Prestamo import Prestamo

class pruebas(unittest.TestCase):
    def test_function_1(self):
        prestamo = Prestamo()
        valor1 = prestamo.valor_total(20000000000, 2)
        valor2 = None
        self.assertEqual(valor1, valor2)
    def test_function_2(self):
        prestamo = Prestamo()
        valor1 = prestamo.valor_total(0, 2)
        valor2 = None
        self.assertEqual(valor1, valor2)
    def test_function_3(self):
        prestamo = Prestamo()
        valor1 = round(prestamo.valor_total(4999.99, 2), 2)
        valor2 = 5201.99
        self.assertEqual(valor1, valor2)
    def test_function_4(self):
        prestamo = Prestamo()
        valor1 = round(prestamo.valor_total(5000, 2), 2)
        valor2 = 5278.75
        self.assertEqual(valor1, valor2)
    def test_function_5(self):
        prestamo = Prestamo()
        valor1 = round(prestamo.valor_total(9999.99, 2), 2)
        valor2 = 10557.49
        self.assertEqual(valor1, valor2)


if __name__ == '__main__':
    unittest.main() 
