def division():
    dividendo=input("Dime el dividendo: ")
    divisor=input("Dime el dividendo: ")
    r=0
    suma_cociente=divisor
    cociente=0
    while suma_cociente<=dividendo:
        cociente=cociente+1
        suma_cociente=suma_cociente+divisor
    print cociente
    r=suma_cociente-dividendo-divisor
    print r
division()
        
