def cuenta_cifras(numero):
    n_cifras=0
    while numero>0:
        numero=numero/10
        n_cifras=n_cifras+1
    return n_cifras


def ordenadorvectores():
    numero=input("Dime un numero de tres cifras: ")
    L=[]
    while numero>0:
        aux=numero%10
        L.append(aux) #Te mete todo el aux#
        numero=numero/10
    L.sort(reverse=False) #Este comando te ordena los numeros de una lista de menor a mayor
    print L
    L.sort(reverse=True) #Este comando te ordena los numeros de una lista de mayor a menor
    print L
ordenadorvectores()


