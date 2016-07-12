import unittest
# Create your tests here.
from Prestamo import Prestamo

# Creando casos de prueba
class TestPrestamo(unittest.TestCase):

    def setUp(self):
        self.prestamo = Prestamo()

    def test1(self):
    	self.assertEqual(self.prestamo.valor_total(2000,2), 2080.8)

    def test2(self):
    	self.assertEqual(self.prestamo.valor_total(5000,6), 5536.25)

    def test3(self):
    	self.assertEqual(self.prestamo.valor_total(12000,5), 13416.0)

    def test4(self):
    	self.assertEqual(self.prestamo.valor_total(21000,10), None)

if __name__ == '__main__':
	unittest.main()