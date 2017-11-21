def Suma2 (n):
    n=n+2
    return n
s='si'
while s!='no':
    numero=input("Dame y le sumo 2: ")
    respuesta= Suma2(numero)
    print respuesta
    s=raw_input ("Continuar: ")

