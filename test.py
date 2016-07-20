import unittest
from prestamo import Prestamo

class TestPrestamo(unittest.TestCase):
    def test_valor1(self):
    	p = Prestamo()
    	""" Inferior a 5000 y tiempo inferior a 3 meses"""
        self.assertEqual(p.valor_total(1000, 2), 1040.4)
    def test_valor2(self):
    	p = Prestamo()
        """ Entre 5000 y 9999.99 y tiempo inferior a 6 meses"""
        self.assertEqual(p.valor_total(5000, 2), 5278.75)
    def test_valor3(self):
    	p = Prestamo()
    	""" Entre 10000 y 20000 y tiempo inferior a 12 meses"""
        self.assertEqual(p.valor_total(10000, 2), 10712)
    def test_valor4(self):
    	p = Prestamo()
    	""" mayor a 20000 """
        self.assertEqual(p.valor_total(30000, 2), None)
    def test_valor5(self):
    	p = Prestamo()
    	""" Inferior a 5000 y tiempo inferior a 3 meses invalido """
        self.assertTrue(p.valor_total(1000, 3), 1020)
    def test_valor6(self):
    	p = Prestamo()
    	""" Entre 5000 y 9999.99 y tiempo inferior a 6 meses invalido """
        self.assertTrue(p.valor_total(6000, 3), 6215.10)
if __name__ == '__main__':
    unittest.main()
