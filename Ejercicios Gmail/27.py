def nmd():
    n=input("NUMERO:")
    cont=1
    suma=0
    while cont<n:
        if n%cont==0:
            suma=suma+cont
        cont=cont+1
    print n
    if suma==n:
        print "Numero perfecto"
    else:
        print "Numero no perfecto"
nmd()
