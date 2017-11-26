#Programa que, introduciendo un numero, muestra la suma de cifras pares, impares, pares e impares por su posicion; la mayor de sus cifras
#y el numero ordenado por sus cifras de menor a mayor
def calculadora():
    cifras= []
    pares=0
    impares=0
    c_impares=0
    c_pares=0
    inverso=0
    n_original=input("Dime un numero cualquiera: ")
    numero=n_original
    while numero>10:
        resto=numero%10
        cifras.append(resto)
        numero=numero/10
    cifras.append(numero)
    n_cifras=len(cifras)
    for cont in range (0,n_cifras,1):
        #Suma de cifras pares segun su posicion
        if cont%2==0:
            pares=pares+cifras[cont]
        #Suma de cifras impares segun su posicion
        else:
            impares=impares+cifras[cont]
        #Suma de cifras pares
        if cifras[cont]%2==0:
            c_pares=c_pares+cifras[cont]
        #Suma de cifras impares 
        else:
            c_impares=c_impares+cifras[cont]
    #Cifra mayor del numero
    cifras.sort()
    #Numero ordenado por sus cifras de menor a mayor
    for cont in range (0,n_cifras,1):
        inverso=(inverso*10)+cifras[cont]
    print "\n\n El numero introducido es: ",n_original    
    print "La suma de los numeros cuya posicion es par es: ",pares
    print "La suma de los numeros cuya posicion es impar es: ",impares
    print "La suma de los numeros pares es: ",c_pares
    print "La suma de los numeros impares es: ",c_impares
    print "La cifra mayor del numero es: ",max(cifras)
    print "El numero ordenado de menor cifra a mayor cifra es: ",inverso   
calculadora()
    
