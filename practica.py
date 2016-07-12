class Prestamo():
	def valor_total(self,prestamo,tiempo):
		# 2% comision 1% interes 3 meses
		if(prestamo>0 and tiempo>0):
			if(prestamo<5000 and tiempo<=3):
				comision=(prestamo *2)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1)/100)*tiempo)
				return float(capital_total+interes)
			# 3% comision 1.25% interes 6 meses
			elif(prestamo<10000 and tiempo<=6):
				comision=(prestamo*3)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1.25)/100)*tiempo)
				return float(capital_total+interes)
			# 4% comision 1.5% interes 12 meses
			elif(prestamo<20000 and tiempo<=12):
				comision=(prestamo*4)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1.5)/100)*tiempo)
				return float(capital_total+interes)
			else:
				print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
				return None
