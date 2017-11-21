def leedor():
    L=[55,57,60,65,70,124,0]
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
def crecien():
    L=[55,57,60,65,70,124,0]
    n=0
    nocon=0
    while L[n]!=0:
        if L[n]<L[n+1]:
            print L[n]
            print L[n+1]
            nocon=1
        n=n+1
    if nocon==1:
        print "lista no creciiente"
    else:
        print "lista creciente"
crecien()

