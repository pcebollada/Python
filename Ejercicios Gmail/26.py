def contador():
    numero=input("Dime un numero: ")
    cifra=0
    n=1
    while n<numero:
        cifra=cifra+1
        n=n*10
    print cifra
contador()
