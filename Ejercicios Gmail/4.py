#diametro pizza en centimetros precio en euros nos de precio c2 de pizza
import math

def pizzeria():
    diametro=input("Dime el diametro de la pizza en centimetros: ")
    precio=input("Dime el precio de la pizza: ")
    calculo_area=((diametro/2)**2)* math.pi
    calculo_definitivo=precio/calculo_area
    print calculo_definitivo
pizzeria()
