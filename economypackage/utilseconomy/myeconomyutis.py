def divisaConverter(money,valueOfTheMoment): 
    if(money==0 or money==0.0): 
        raise Exception("El valor del dinero introducido esta vacio")
    else:
        return round(money*valueOfTheMoment)