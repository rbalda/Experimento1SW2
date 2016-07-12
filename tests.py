import unittest
from prestamo import Prestamo

class ValidarPrestamo(unittest.TestCase):

	def test_valor_total_1(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(2500,2), 2601.0)

	def test_valor_total_2(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(7500,5), 8207.8125)

	def test_valor_total_3(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(15000,9), 17706.0)

	def test_valor_total_4(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(22000,6), None)
	
if __name__ == '__main__':
	unittest.main()