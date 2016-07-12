import unittest
from programa import Prestamo

class PrestamoTestCase(unittest.TestCase):

    def setUp(self):
        """se la llama antes de cada test"""
        self.prestamo = Prestamo()

    def tearDown(self):
        """llamar luego de cada test"""
        print("termino test")

    def testA(self):
        """test de prestamo < 5000 tiempo=3"""
        assert self.prestamo.valor_total(20,3) == 20.6
    def testB(self):
        """test de prestamo entre 5000 y 9999.99 tiempo maximo de 6"""
        assert self.prestamo.valor_total(6000,6) == 6643.5

    def testC(self):
        """test de prestamo entre 10000 y 20000 tiempo maximo de 12"""
        assert self.prestamo.valor_total(16000,12) == 19635.2

    def testD(self):        
        """test prestamo > 20000"""
        assert self.prestamo.valor_total(25000,13) == None

    def testE(self):        
        """tiempo negativo"""
        assert self.prestamo.valor_total(25000,-13) == None

if __name__ == "__main__":
    unittest.main() # run all tests
