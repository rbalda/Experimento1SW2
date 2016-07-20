class Prestamo():
	def valor_total(self,prestamo,tiempo):
		if(prestamo>0 and tiempo>0):
			if(prestamo<5000 and tiempo<=3):
				comision=(prestamo *2)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1)/100)*tiempo)
				print("-----------------------------------")
				print ("prestado:",prestamo)
				print ("Capital total:",capital_total)
				print("%de comision:", comision)
				print ("%de interes:", interes)
				return float(capital_total+interes)
			elif(prestamo<10000 and tiempo<=6):
				comision=(prestamo*3)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1.25)/100)*tiempo)
				print("-----------------------------------")
				print ("prestado:",prestamo)
				print ("Capital total:",capital_total)
				print("%de comision:", comision)
				print ("%de interes:", interes)
				return float(capital_total+interes)
			elif(prestamo<20000 and tiempo<=12):
				comision=(prestamo*4)/100
				capital_total=float(prestamo+comision)
				interes=float(((capital_total*1.5)/100)*tiempo)
				print("-----------------------------------")
				print ("prestado:",prestamo)
				print ("Capital total:",capital_total)
				print("%de comision:", comision)
				print ("%de interes:", interes)
				return float(capital_total+interes)
			else:
				print("-----------------------------------")
				print("RECHAZADO")
				print ("Capital prestado:",prestamo)
				print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
				return None
