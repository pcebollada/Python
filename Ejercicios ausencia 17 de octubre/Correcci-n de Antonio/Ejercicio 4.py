def sumador_digitos():
    numero=input("Introduce un número de dos dígitos: ")
    decenas= numero/10
    unidades= numero - 10*decenas #n%10#
    print decenas
    print unidades
    print "La suma de las cifras de",numero,"vale",decenas + unidades
sumador_digitos()

#def sumador_digitos2():        
    #numero=input("Dime un numero de seis digitos: ")
    #centenas=numero/100
    #decenas=numero%centenas - (10*decenas + unidades)
    #unidades=numero%centenas - 10*decenas
    #print centenas
    #print decenas
    #print unidades
#sumador_digitos2()

def sumador_digitos2():
    suma=0
    numero=input("Dime un numero de seis digitos: ")
    while numero>10:
        suma=suma + numero%10
        numero=numero/10
    print "La suma de los dígitos es",suma+numero
sumador_digitos2()
