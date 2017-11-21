def invertidor():
    L=[]
    n=input("Dime el numero que quieras: ")
    while n>10:
        resto=n%10
        L.append(resto)
        n=n/10
    L.append(n)
    print L
invertidor()
