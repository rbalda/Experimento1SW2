import unittest
from tarea import Prestamo

class TestFinanciero(unittest.TestCase):
    def setUp(self):
        self.prestamo = Prestamo()
 
    def test_1(self):
        self.assertEqual(self.prestamo.valor_total(2000,2), 2080.8)
 
    def test_1_25(self):
        self.assertEqual(self.prestamo.valor_total(6000,4), 6489.0)

    def test_1_5(self):
        self.assertEqual(self.prestamo.valor_total(15000,6), 17004.0)

if __name__ == '__main__':
	unittest.main()