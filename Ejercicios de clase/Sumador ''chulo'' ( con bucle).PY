def sumador_chulo():
    n=input("Dame un numero hasta el que desees sumar")
    r=0
    for cont in range (1,n+1,1):
        r=cont+r
    print ("El resultado es", r)
sumador_chulo()
