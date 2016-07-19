import unittest
import Prestamo # code from module you're testing


class SimpleTestCase(unittest.TestCase):

    def test_caso1(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(-10,2), None)
		
    def test_caso2(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(2000,2), 2080.8)
		
    def test_caso1(self):
		prestamo = Prestamo()
		self.assertEqual(prestamo.valor_total(22000,5), None)
		
		
if __name__ == '__main__':
    unittest.main() # run all tests