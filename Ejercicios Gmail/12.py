#30 dólares si el coche lleva mal aparcado más de 1 hora
#aparcar mal menos de 1 hora no es una infracción
#suplemento de 5 dolares por hora si la infracción supera las 24 horas
# programa del tiempo que lleva mal estacionado, diciendo si es o no infracción
#y coste
def chivato():
    n=input("Dime cuanto lleva mal aparcado en horas: ")
    if n<1:
        print "No es una infraccion"
    elif n>1 and n<24:
        multa=30
        print "Es una infraccion"
        print "La multa seran",multa,"euros"
    elif n>24:
        multa2= 30+ (n-24)*5
        print "Es una infraccion"
        print "La multa seran",multa2,"euros"
chivato()
