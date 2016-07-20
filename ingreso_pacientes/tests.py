from django.test import TestCase

# Create your tests here.
from capital import Prestamo

# Creando casos de prueba
class CrearPrestamo(TestCase):

	def crear_prestamo(self):
		self.prestamo = Prestamo()

	#CE1 0 < Capital < 5000
	 # ***Prueba No Exitosa***
	def test_prestamo_inferior_a_5000(self):
		total = self.crear_prestamo().valor_total(2000, 4)
		self.assertTrue(total, 2000.0)
	# ***Prueba Exitosa***
	def test_prestamo_inferior_a_5000(self):
		total = self.crear_prestamo().valor_total(2000, 2)
		self.assertTrue(total, 2080.8)
	#CE2 5000 < Capital < 10000
	# ***Prueba Exitosa***
	def test_prestamo_entre_5000_valido(self):
		total = self.crear_prestamo().valor_total(6000, 5)
		self.assertTrue(total, 6566.25)
	# ***Prueba No Exitosa***
	def test_prestamo_entre_5000(self):
		total = self.crear_prestamo().valor_total(5000, 7)
		self.assertTrue(total, None)
	# ***Prueba No Exitosa***
	def test_prestamo_entre_10000(self):
		total = self.crear_prestamo().valor_total(10000, 14)
		self.assertTrue(total, None)
	#CE3 10000 < Capital < 20000
    # ***Prueba Exitosa***
    def test_prestamo_entre_10000(self):
		total = self.crear_prestamo().valor_total(10000, 7)
		self.assertTrue(total, 10556)
	# ***Prueba No Exitosa***
    def test_prestamo_entre_10000_valido(self):
		total = self.crear_prestamo().valor_total(10000, 12)
		self.assertTrue(total, 12272.0)
	#CE3  Capital > 20000
	def test_prestamo_mayor_20000(self):
		total = self.crear_prestamo().valor_total(21000, 1)
		self.assertTrue(total, None)