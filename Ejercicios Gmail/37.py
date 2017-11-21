def leedor():
    L=[55,-78,43,22,10,57,124,0]
    n=0
    negativo=0
    while L[n]!=0:
        if L[n]<0:
            negativo=1
        n=n+1
    if negativo==0:
        print"todos son positivos"
    else:
        print"algun numero es negativo"
leedor()

