import unittest
from Prestamos import Prestamo

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        self.prestamo = Prestamo()

    def testA(self):
        #Prueba ejemplo de la hoja
        assert Prestamo.valor_total(self, 2000, 2) == 2080.8

    def testB(self):
        #Prueba con capital menor a 5000, 3 meses
        assert Prestamo.valor_total(self, 4999, 3) == 5251.9493999999995

    def testC(self):
        #Prueba con capital entre 5000 a 10000, 5 meses
        assert Prestamo.valor_total(self, 8000, 5) == 8755

    def testD(self):
        #Prueba con capital entre 10000 y 20000, 10 meses
        assert Prestamo.valor_total(self, 12000, 10) == 14352

    def testE(self):
        #Prueba con capital mayor a 20000, 5 meses
        assert Prestamo.valor_total(self, 20001, 5) == None

if __name__ == "__main__":
    unittest.main()
