def multiplicador():
    n= input ("Dime la tabla de multiplicar que deseas que escriba:")
    print"LA TABLA DEL",n
    for cont in range (1,11,1):
        print n,"*",cont,"=",n*cont
multiplicador()
