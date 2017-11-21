#programa lea numero entero no negativo N, y escriba una lista con N 1ªs pot. de 2
def elevador():
    N=input("Dime un numero no negativo: ")
    for cont in range (1,N+1,1):
        resultado=2**cont
        print resultado
elevador()
