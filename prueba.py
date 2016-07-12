import unittest
from practica import Prestamo


class AddTest(unittest.TestCase):

   def setUp(self):
      self.prestamo = Prestamo()
      pass
   def tearDown(self):
      pass
   def test_prestamo_menor0(self):
       self.assertEqual(self.prestamo.valor_total(-10,2),None)
   def test_tiempo_menor0(self):
       self.assertEqual(self.prestamo.valor_total(1000,-2),None)
   def test_prestamo_menor5000(self):
       self.assertEqual(self.prestamo.valor_total(2000,2),2080.8)
   def test_prestamo_menor10000(self):
       self.assertEqual(self.prestamo.valor_total(6000,5),6566.25)
   def test_prestamo_menor20000(self):
       self.assertEqual(self.prestamo.valor_total(15000,11),18174.0)
   def test_prestamo_mayor20000(self):
       self.assertEqual(self.prestamo.valor_total(21000,12),None)
if __name__=='__main__':
   unittest.main()
