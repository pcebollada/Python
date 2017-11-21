def leedor():
    L=[55,78,43,22,10,57,124,0]
    n=0
    mayor=0
    menor=0
    while L[n]!=0:
        if L[n]>L[mayor]:
            mayor=n
        if L[n]<L[menor]:
            menor=n
        n=n+1
    print L[mayor]
    print L[menor]
    print n
leedor()

