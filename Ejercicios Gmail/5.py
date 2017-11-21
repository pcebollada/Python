#modificar programa para pedir datos sobre dos pizzas y decir la mas barata
import math

def pizzeria_2():
    dm=input("Dime el diametro de la pizza margarita en centimetros: ")
    pm=input("Dime el precio de la pizza margarita: ")
    dce=input("Dime el diametro de la pizza cuatro estaciones en centimetros: ")
    pce=input("Dime el precio de la pizza cuatro estaciones: ")
    calculo_area_m=((dm/2)**2)* math.pi
    calculo_definitivo_m=pm/calculo_area_m
    calculo_area_ce=((dce/2)**2)* math.pi
    calculo_definitivo_ce=pce/calculo_area_ce
    if calculo_definitivo_m>calculo_definitivo_ce:
        print "La mas barata es la cuatro estaciones"
    else:
        print "La mas barata es la margarita"

pizzeria_2()
