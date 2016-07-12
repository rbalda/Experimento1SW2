import unittest
# import Prestamo
from Prestamo import Prestamo

class TestStringMethods(unittest.TestCase):
    def test_Prestamo(self):
        p = Prestamo();
        self.assertEqual(p.valor_total(4000, 2), 4161.6)
    def test_upper(self):
        p = Prestamo();
        self.assertEqual(p.valor_total(6000, 5), 6566.25)
    def test_upper(self):
        p = Prestamo();
        self.assertEqual(p.valor_total(15000, 10), 17940.0)
    def test_upper(self):
        p = Prestamo();
        self.assertEqual(p.valor_total(22000, 10), None)

if __name__ == '__main__':
    unittest.main()
