#Dados hipotenusa y catetos saber si el numero es o no un triangulo rectangulo
#a**2= b**2+c**2 SOLO si es rectangulo
def comprobador():
    h=input("Dime el valor de la hipotenusa")
    c1=input("Dime el valor del primer cateto")
    c2=input("Dime el valor del segundo cateto")
    if h**2==c1**2 + c2**2:
        print "Este triangulo es un triangulo rectangulo"
    if h**2!=c1**2 + c2**2:
        print "Este triangulo no es un triangulo rectangulo"
comprobador()

#en un if se pueden poner variables y operaciones dentro
#otra forma sería crear una variable que contenga el cálculo del cuadradado
#de la hipotenusa, y otra variable que contenga el otro cálculo, y luego
#comparar. Sería lo mismo.

#que es un ordenador, informatica, variable, programa,sistema operativo,
#que es un algoritmo,lenguaje de programación,diagrama de flujo,
#tipos de variables(contadora,acumuladora,multiplicadora,...)
#operadores logicos, AND, OR, diferencia entre == e =
#for, while
#que diferencia hay un if de rama simple, y un if de rama compuesta

#Uno de rama simple tienes una condición que se valora. Hay dos posibilidades,
#VERDADERO O FALSO. Si es verdadero, podemos decirle que haga algo. Y si es
#falso, el programa acabara sin hacer nada.
#Si por ejemplo se establece una condición para cuando no se cumple,
#entonces sería uno de doble rama.
