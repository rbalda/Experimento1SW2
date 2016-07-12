class Prestamo():
	def valor_total(self,prestamo,tiempo):
        	if( prestamo <5000 && tiempo <=3):
                comision=(prestamo *2)/100
                capital_total=float(prestamo+comision)
                interes=float(((capital_total*1)/100)*tiempo)
                return float(capital_total+interes)
            if(prestamo <9999.99 && tiempo <=6):
                comision=(prestamo*3)/100
                capital_total=float(prestamo+comision)
                interes=float(((capital_total*1.25)/100)*tiempo)
                return float(capital_total+interes)
            if(prestamo <20000 && tiempo <=12):
                comision=(prestamo*4)/100
                capital_total=float(prestamo+comision)
                interes=float(((capital_total*1.5)/100)*tiempo)
                return float(capital_total+interes)
            if(prestamo <5000 && tiempo <=3):
                print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
                return None
