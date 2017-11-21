# -*- coding: cp1252 -*-
#hacer un programa que segun la hora que sea, nos diga buenos dias, buenas tardes o buenas noches#
#De seis a catorce, son buenos días;de catorce a veinte son buenas tardes; y de 20 a 6 son buenas noches#
def saludador():
    h=input("Dime que hora es?:")
    if (h>=6 and h<14):
        print "Buenos dias"
    elif (h>=14 and h<20):
        print "Buenas tardes"
    elif ((h>=20 and h<=24) or (h>=0 and h<6)):
        print "Buenas noches"
saludador()
