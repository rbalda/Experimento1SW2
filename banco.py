import unittest

class Prestamo():
	"""
	Autor: Erika Narvaez
	Nombre de funcion: valor_total
	Entrada: valor del prestamo, y tiempo de plazo
	Salida: capital total a devolver al banco
	Descripcion: Funcion que realiza los respectivos calculos para obtener el valor a pagar del prestamo pedido en un tiempo plazo.
	"""
	def valor_total(self,prestamo,tiempo):
		if(prestamo > 0 and prestamo < 5000 and tiempo <= 3 and tiempo >= 0 and isinstance(tiempo, int)):
			comision=(prestamo *2)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo > 5000 and prestamo < 10000 and tiempo <= 6 and isinstance(tiempo, int)):
			comision=(prestamo*3)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.25)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo >= 10000 and prestamo <= 20000 and tiempo <= 6 and isinstance(tiempo, int)):
			comision=(prestamo*4)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.5)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo > 20000 and tiempo > 0 and isinstance(tiempo, int)):
			print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
			return None
		if(prestamo <= 0 or tiempo < 0 or not isinstance(tiempo, int)):
			print("datos del prestamo son invalidos")
			return None

class AddTest(unittest.TestCase):
	def setUp(self):
		self.prestamo = Prestamo()

	def test_prestamo_positivo_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(2000,2), 2080.8)
		
	def test_prestamo_5008_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(5008,2), 5287.196)
	
	def test_prestamo_12008_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(12008,2), 12862.9696)

	def test_prestamo_excede_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(22000,6), None)

	def test_prestamo_negativo_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(-2000,2), None)

	def test_tiempo_negativo_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(2000,-2), None)

	def test_tiempo_no_entero_valor_total(self):
		self.assertEqual(self.prestamo.valor_total(2000,2.5), None)

if __name__ == "__main__":
	unittest.main()


