# este programa pide dos numeros y los suma #
def calculadora():
    print "Introduce un numero"
    a = input()
    print "Introduce otro numero"
    b = input()
    if a > b :
        c = a - b
        print "El resultado de la resta es", c
    else:
        c = a + b
        print "El resultado de la suma es", c
calculadora()


