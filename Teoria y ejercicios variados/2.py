n=0
def pepe():
    print "hola"
    print "adios"
    j=10
    return j

n= pepe()
print n #sacamos la variable j de la funcion y luego la asignamos a n
        #si imprimieramos j, nos saldría error xq le hemos cambiado el nombre
pepe ()
print n

def pepa(n2):
    print "hola"
    print "adios"
    j=n2+1
    return j

r= pepa (n)# r es: el valor de return cuando la variable n2=n
print r

r= pepa (2)
print r

print "dime n"
n=input()
print n



n=input("dime n")
print n
#es lo mismo, pero uso mas el segundo
#RAW_INPUT NO ES PARA NUMEROS

# ** #ELEVAR UN NUMERO
# *  #MULTIPLICAR
# +
# -
# /
# %  #RESTO
# // DIVIDIR TRUNCANDO

X="HOLA"
n=0
y=1.0
z=232323232323323232323232323234456765456556765434567654345

print type(X) #esta función sirve para ver que tipo de variable es la escrita
print type(n) #es 'int' por ser numero pequeño, natural  
print type(y) #es 'float' por ser un numero decimal
print type(z) #es 'long' por ser un numero muy grande


