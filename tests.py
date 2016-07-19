import unittest

from prestamo import Prestamo


class prestamoTestCase(unittest.TestCase):

    def test_calcular_valor1(self):
        self.prestamo = Prestamo.objects.create(4000,3)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)

    def test_calcular_valor2(self):
        self.prestamo = Prestamo.objects.create(6000,6)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)

    def test_calcular_valor3(self):
        self.prestamo = Prestamo.objects.create(10000,12)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)

    def test_calcular_valor4(self):
        self.prestamo = Prestamo.objects.create(30000,13)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)

    def test_calcular_valor5(self):
        self.prestamo = Prestamo.objects.create(30000,-1)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)

    def test_calcular_valor6(self):
        self.prestamo = Prestamo.objects.create(40000,14)
        self.calcularValor()
        self.assertIsInstance(self.prestamo,Prestamo)








