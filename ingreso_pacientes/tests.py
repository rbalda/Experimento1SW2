import unittest
from prestamo import Prestamo


class prestamo(unittest.TestCase):
    """ PRUEBA 1
    clase de equivalencia
    prestamo menor a 5000 y tiempo = 3"""
    def crear_prestamo(self):
        persona1=Prestamo()
        persona1.valor_total(2000, 3)


class prestamo2(unittest.TestCase):
    """ PRUEBA 2
    clase de equivalencia
    prestamo IGUAL a 5000 y tiempo = 6"""
    def crear_prestamo(self):
        persona2=Prestamo()
        persona2.valor_total(5000, 3)

class prestamo3(unittest.TestCase):
    """ PRUEBA 3
    clase de equivalencia
    prestamo entre 5000 y 9999,99 y tiempo 6"""
    def crear_prestamo(self):
        persona3=Prestamo()
        persona3.valor_total(5001, 6)

class prestamo4(unittest.TestCase):
    """ PRUEBA 4
    clase de equivalencia
    prestamo entre 5000 y 9999,99 y tiempo 6"""
    def crear_prestamo(self):
        persona4=Prestamo()
        persona4.valor_total(7000, 6)
