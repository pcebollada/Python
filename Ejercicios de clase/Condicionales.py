# este programa pide dos numeros y los suma #
def calculadora():
    print "Introduce un numero"
    a = input()
    print "Introduce otro numero"
    b = input()
    if a == b :
        c = a - b
    else:
        if a > b:
            c = a -b
        else:            
            c = a + b
    print "El resultado es", c
calculadora()


