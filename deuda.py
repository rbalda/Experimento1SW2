def valor_total(prestamo,tiempo):
    if prestamo < 5000:
        comision=(prestamo *2)/100
        capital_total=float(prestamo+comision)
        interes=float(((capital_total*1)/100)*tiempo)
        return float(capital_total+interes)
    elif(prestamo < 10000):
        comision=(prestamo*3)/100
        capital_total=float(prestamo+comision)
        interes=float(((capital_total*1.25)/100)*tiempo)
        return float(capital_total+interes)
    elif(prestamo < 20000):
        comision=(prestamo*4)/100
        capital_total=float(prestamo+comision)
        interes=float(((capital_total*1.5)/100)*tiempo)
        return float(capital_total+interes)
    else:
        print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
        return None
