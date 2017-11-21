def cualessonpares():
    suma=0
    numero=input("Dime un numero de cuatro, cinco o seis cifras: ")
    while numero>10:
        aux=numero%10
        if aux%2==0:
            suma=suma+1
        numero=numero/10
    print "Hay",suma,"numeros pares"
    print "PEPE"
cualessonpares()
#nos piden que cuente los numeros pares
