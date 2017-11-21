#programa lea numero entero y tabla de multiplicar de 0 a 10
def multiplicador():
    numero=input("Dime cualquier numero para hacer su tabla de multiplicar:")
    for cont in range (0,11,1):
        resultado= cont*numero
        print cont,"x",numero,"=",resultado
multiplicador()
