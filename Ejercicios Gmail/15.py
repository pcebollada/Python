#programa dado un número que sean segundos, devuelva dias horas minutos...
def calculador_horas():
    n=input("Dime una cantidad de segundos")
    while n>0:
        resultado=n/60
        resto=n%60
    print resto
calculador_horas
