def producto_sin_x():
    n=-1
    m=-1
    while  n<0:
        n=input("Dime un numero positivo: ")
        if n<0:
            print "este numero es negativo"
    while m<0:
        m=input("Dime otro numero positivo: ")
    suma=0
    cont=0
    while cont<m:
        suma=suma+n
        cont=cont+1
    print suma
producto_sin_x()
