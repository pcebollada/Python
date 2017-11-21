def clasificador_numeros():
    x=input("dime un numero")
    y=input ("dime otro numero")
    if ((x%2==0)and(y%2==0)):
        print "Los numeros son pares"
    if ((x%2==1)and(y%2==1)):
        print "Los numeros son impares"
    if (((x%2==1)and (y%2==0))or(x%2==0)and (y%2==1)):
        print "Un numero es par y el otro impar"
clasificador_numeros()
    
