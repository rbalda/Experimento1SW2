import unittest
from codigo import Prestamo


class AddTest(unittest.TestCase):

   def setUp(self):
      self.prestamo = Prestamo()
      pass
   def tearDown(self):
      pass
   def test_prestamoMenorCero(self):
       self.assertEqual(self.prestamo.valor_total(-1,1),None)
   def test_tiempoMenorCero(self):
       self.assertEqual(self.prestamo.valor_total(300,-1),None)
   def test_prestamoMenor5000(self):
       self.assertEqual(self.prestamo.valor_total(3400,3),3572.04)
   def test_prestamoMenor10000(self):
       self.assertEqual(self.prestamo.valor_total(9000,4),9733.5)
   def test_prestamoMenor20000(self):
       self.assertEqual(self.prestamo.valor_total(17800,10),21288.8)
   def test_prestamoMayor20000(self):
       self.assertEqual(self.prestamo.valor_total(20001,12),None)
if __name__=='__main__':
   unittest.main()
