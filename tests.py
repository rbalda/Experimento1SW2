#from django.test import TestCase
import unittest
# Create your tests here.
# from ingreso_pacientes.models import Prestamo
class Prestamo():
	"""
	Autor: Erika Narvaez
	Nombre de funcin: valor_total
	Entrada: valor del prestamo, y tiempo de plazo
	Salida: capital total a devolver al banco
	Descripcion: Funcion que realiza los respectivos calculos para obtener el valor a pagar del prestamo pedido en un tiempo plazo.
	"""
	def valor_total(self,prestamo,tiempo):
		if(prestamo < 5000 and tiempo <= 3):
			comision=(prestamo *2)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo >= 5000 and prestamo < 10000 and tiempo <= 6):
			comision=(prestamo*3)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.25)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo >= 10000 and prestamo <= 20000 and tiempo <= 12):
			comision=(prestamo*4)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.5)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo > 20000):
			print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
			return None

# Creando casos de prueba
class CrearPrestamo(unittest.TestCase):

	def crear_prestamo(self):
		self.prestamo = Prestamo()
		return self.prestamo

	def test_prestamo_inferior_a_5000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(2000, 4)
		self.assertEqual(total, None, "El banco no puede otorgar dicho prestamo ya que excede al monto definido")

	def test_prestamo_inferior_a_5000_mes_valido(self):
		total = self.crear_prestamo().valor_total(2000, 3)
		self.assertEqual(total, 2101.2, None)

	def test_prestamo_entre_5000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(5000, 7)
		self.assertEqual(total, None, None)

	def test_prestamo_entre_5000_mes_valido(self):
		total = self.crear_prestamo().valor_total(5000, 4)
		self.assertEqual(total, 5407.5, None)

	def test_prestamo_entre_10000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(10000, 14)
		self.assertEqual(total, None, None)

	def test_prestamo_entre_10000_mes_valido(self):
		total = self.crear_prestamo().valor_total(10000, 12)
		self.assertEqual(total, 12272.0, None)

	def test_prestamo_mayor_20000(self):
		total = self.crear_prestamo().valor_total(21000, 1)
		self.assertEqual(total, None, None)

if __name__ == "__main__":
	unittest.main()
