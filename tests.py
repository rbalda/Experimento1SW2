import unittest

from prestamo import Prestamo


class prestamoTestCase(unittest.TestCase):

    def setUp(self):
        self.prestamo = Prestamo()

    def test_calcular_valor1(self):
        self.assertEquals(self.prestamo.valor_total(2000,2),2080.8)

    def test_calcular_valor2(self):
        self.assertEquals(self.prestamo.valor_total(5008,2),5286.95)

    def test_calcular_valor3(self):
        self.assertEquals(self.prestamo.valor_total(12008,2),12862.64)

    def test_calcular_valor4(self):
        self.assertEquals(self.prestamo.valor_total(30000,7),None)


if __name__ == "__main__":
    unittest.main()





