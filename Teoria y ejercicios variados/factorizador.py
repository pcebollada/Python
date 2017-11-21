#Dado un numero factorizar y decir todos sus factores
#Condicion resto=0
#cont
def factorizador():
    n=input("Dime un numero")
    for cont in range (1,n+1,1):
        if n%cont==0:
            print "Los factores son",cont
        else:
            print "Vuelve a intentarlo"
factorizador()
#else es para, dentro de un if, decirle al programa que hacer si no se
#cumpla esa condicion, hacer otra cosa
def factorizador():
    n=input("Dime un numero")
    for cont in range (2,n+1,1):
        if n%cont==0:
            print "Los factores son",cont
            n=n/cont

    n=input("Dime un numero")
    cont=2
    while cont<=n+1:
        if n%cont==0:
            print "Los factores son",cont
            n=n/cont
        else:
            cont=cont+1
factorizador()
