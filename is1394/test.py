import unittest
from prestamo import Prestamo

"""
    Clases de equivalencia de las variables
    variable prestamo y variable tiempo

    Variable prestamo
    CE | Descripcion | Validez
    1  | valor decimal positivo |valido
    2  | valor no decimal positivo | invalido
    3  | prestamo < 5000 | valido
    4  | 5000 < prestamo < 9999.99 | valido
    5  | 10000 < prestamo < 20000 | valido
    6  | prestamo > 20000 | invalido


    Variable tiempo
    CE | Descripcion | Validez
    1  | valor entero <= 12 |valido
    2  | valor no entero | invalido
"""
class PrestamoTest(unittest.TestCase):
    """
        Autor: Israel Fernandez
        Descripcion: Clase que ejecuta casos de Prueba de la clase Prestamo
    """

    def setUp(self):
        self.prestamo = Prestamo()

    def test1(self):
        """
            Test capital menor 5000 y tiempo menor 3
            prestamo = 2000
            tiempo  = 2
            resultado esperado 2080.8
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=2000,tiempo =2)
        except:
            print "Ops algo salio mal"
        assert result == 2080.8

    def test2(self):
        """
            Test capital entre 5000 y 9999.99 con tiempo menor a 6
            prestamo = 6000
            tiempo  = 5
            resultado esperado 6566.25
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=6000, tiempo=5)
        except:
            print "Oops algo salio mal"
        assert result == 6566.25

    def test3(self):
        """
            Test capital entre 10000 y 20000 con tiempo menor a 12
            prestamo = 11000
            tiempo  = 10
            resultado esperado 13156.0
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=11000, tiempo=10)
        except:
            print "Oops algo salio mal"
        assert result == 13156.0

    def test4(self):
        """
            Test capital excede 20000 con tiempo menor a 12
            prestamo = 22000
            tiempo  = 6
            resultado esperado None (El banco no puede otorgar dicho prestamo)
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=22000, tiempo=6)
        except:
            print "Oops algo salio mal"
        assert result == None

    def test5(self):
        """
            Test capital esta dentro de los valores permitidos y tiempo mayor 12
            prestamo = 4000
            tiempo  = 14
            resultado esperado None (El tiempo seleccionado no es el adecuado)
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=4000, tiempo=14)
        except:
            print "Oops algo salio mal"
        assert result == None

    def test6(self):
        """
            Test capital valor negativo y tiempo dentro de los valores permitidos
            prestamo = -2000
            tiempo  = 5
            resultado esperado None (El tiempo seleccionado no es el adecuado)
        """
        result = None
        try:
            result = self.prestamo.valor_total(prestamo=-2000, tiempo=5)
        except:
            print "Oops algo salio mal"
        assert result == None


if __name__ == "__main__":
    unittest.main() # run all tests
