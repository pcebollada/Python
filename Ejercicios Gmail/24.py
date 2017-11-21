def nmd():
    n=input("NUMERO:")
    cont=1
    numd=0
    while cont<n:
        if n%cont==0:
            numd=cont
        cont=cont+1
    print numd
nmd()
