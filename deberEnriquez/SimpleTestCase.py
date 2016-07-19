import unittest
import Prestamo # code from module you're testing
from django.test import TestCase


class SimpleTestCase(unittest.TestCase):

    def test_caso1(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(-10,2), None)
		
    def test_caso2(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(2000,2), 2080.8)
		
    def test_caso3(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(22000,5), None)

    def test_caso4(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(15000,20), None)
	
	def test_caso5(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(6000,7), None)
		
		
if __name__ == '__main__':
    unittest.main() # run all tests