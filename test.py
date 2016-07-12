import unittest
from prestamo import Prestamo
class TestPrestamo(unittest.TestCase):
    def test_valor1(self):
    	p = Prestamo()
    	""" Inferior a 5000 y tiempo inferior a 3 meses"""
        self.assertEqual(p.valor_total(1000,2), 1030)
    def test_valor2(self):
    	p = Prestamo()
    	""" Entre 5000 y 9999.99 y tiempo inferior a 6 meses"""
        self.assertEqual(p.valor_total(5000,2), 5212.5)
    def test_valor3(self):
    	p = Prestamo()
    	""" Entre 10000 y 20000 y tiempo inferior a 12 meses"""
        self.assertEqual(p.valor_total(10000,2), 10550)
    def test_valor4(self):
    	p = Prestamo()
    	""" mayor a 20000 """
        self.assertEqual(p.valor_total(30000,2), none)
    def test_valor5(self):
    	p = Prestamo()
    	""" Inferior a 5000 y tiempo mayor a 3 meses"""
        self.assertEqual(p.valor_total(3000,2), none)
    def test_valor6(self):
    	p = Prestamo()
    	""" Entre 5000 y 9999.99 y tiempo superior a 6 meses"""
        self.assertEqual(p.valor_total(8000,8), none) 
    def test_valor7(self):
    	p = Prestamo()
    	""" Entre 10000 y 20000 y tiempo superior a 12 meses"""
        self.assertEqual(p.valor_total(15000,22), none)
    def test_valor8(self):
    	p = Prestamo()
    	""" Prestamo <= 0 y tiempo < = 0"""
        self.assertEqual(p.valor_total(0,0), none)
    def test_valor9(self):
    	p = Prestamo()
    	""" Prestamo <= 0 y tiempo > 12"""
        self.assertEqual(p.valor_total(0,22), none)

if __name__ == '__main__':
    unittest.main()       