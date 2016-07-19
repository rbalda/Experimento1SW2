class Prestamo():
        
        def valor_total(self,prestamo,tiempo):
                if(prestamo < 5000 and prestamo > 0):
                                comision=(prestamo *2)/100
                                capital_total=float(prestamo+comision)
                                interes=float(((capital_total*1)/100)*tiempo)
                                return float(capital_total+interes)
                if(prestamo > 5000 and prestamo < 9999.99):
                                comision=(prestamo*3)/100
                                capital_total=float(prestamo+comision)
                                interes=float(((capital_total*1.25)/100)*tiempo)
                                return float(capital_total+interes)
                if(prestamo > 5000 and prestamo < 20000):
                                comision=(prestamo*4)/100
                                capital_total=float(prestamo+comision)
                                interes=float(((capital_total*1.5)/100)*tiempo)
                                return float(capital_total+interes)
                if(prestamo > 20000 or prestamo < 0):
                                print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
                                return None
