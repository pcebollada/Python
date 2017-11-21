#cuando nos den la ecuacion, que nos devuelva los factores
##import math
##def ecuacionario():
    ##a=input("Dime el coeficiente del cuadrado: ")
    ##b=input("Dime el coeficiente de la x: ")
    ##c=input("Dime el termino independiente: ")
    ##resultado1=(-b+math.sqrt(b**2-4*a*c)/2*a)
    ##resultado2=(-b-math.sqrt(b**2-4*a*c)/2*a)
    ##print "Las soluciones son (x",resultado1,")","y (x",resultado2,")"
##ecuacionario()

import math

def ecuacionionario():
    a=input("Dime el coeficiente del cuadrado: ")
    b=input("Dime el coeficiente de la x: ")
    c=input("Dime el termino independiente: ")
    contenido_raiz=b**2 - 4*a*c
    if (contenido raiz<0):
        print "La ecuación es de tipo C, no se puede factorizar"
    else (contenido_raiz==0):
        print "Es de tipo b. Corta en el putno",-b/2*a
    else:
        print "Es de tipo a. Corta en los ptnos ", -b
