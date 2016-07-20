import unittest
from prestamo import Prestamo
class TestPrestamo(unittest.TestCase):
    def test_valor1(self):
		p = Prestamo()
		""" Inferior a 5000 y tiempo inferior a 3 meses"""
        total = p.valor_total(1000,2)
		self.assertEqual(total, 1040.4)
    def test_valor2(self):
		p = Prestamo()
        """ Entre 5000 y 9999.99 y tiempo inferior a 6 meses"""
        total = p.valor_total(5000,2)
		self.assertEqual(total, 5278.75)
    def test_valor3(self):
		p = Prestamo()
		""" Entre 10000 y 20000 y tiempo inferior a 12 meses"""
        total = p.valor_total(10000,2)
		self.assertEqual(total, 10712)
    def test_valor4(self):
		p = Prestamo()
		""" mayor a 20000 """
        total = p.valor_total(30000,2)
		self.assertEqual(total, None)
if __name__ == '__main__':
    unittest.main()
