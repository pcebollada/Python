def uno():
    n=input("Dime un numero")
    cont=0
    m=10
    while n>10:
        if n%m==1:
            cont=cont+1
        print n%m
        n=n/m
    if n==1:
        cont=cont+1
    print cont
uno()
