def sumador_impares():
    n1=input("Dime un primer numero: ")
    n2=input("Dime un segundo numero: ")
    suma=0
    for cont in range ((n1),((n2)+1),1):
        if cont%2==1:
            suma=suma+cont
    print suma
sumador_impares()

#def sumador_impares_2():
    #n1=input("Dime un primer numero: ")
    #n2=input("Dime un segundo numero: ")
    #suma=0
    #while n1<n2:
        #if n1%2==1:
            #suma=suma+n1
        #n1=n1+1
    #print suma
#sumador_impares_2()
