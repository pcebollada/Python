variable=3
for variable in range(0,10,1):
    print variable

variable=11 
while variable<=10:
    print variable
    variable=variable+1

variable=0
while variable!=10:
    print variable
    variable=variable+1
#== >= <= !=

#for
#while - poner v=0; v=v+1; condicion

L=[0,1,2,3,4,5]
#Son mutables
#-Puedes cambiar cachos
#Puedes volver a definirlas, añadir cosas, eliminar cosas
#Acceder por indice. Se pueden imprimir partes de lista. Posicion empieza por 0
print L
print L[1:5:1]
print L[0:5:2]
print L[-1]
L.append (8)
print L
#NOMBREDELALISTA.append() sirve para añadir un número a esa lista
L[0:4]=[0,0,0,0]
print L
L.pop ()
print L
for c in L:
    print c

#input es para números
#raw_input para strings, palabras
    #Dentro del raw_input y del input se puede poner un print

pregunta="cualquier cosa"
while pregunta!='Si':
    #print "Vas a venir a mi fiesta de cumpleaños?"
    pregunta=raw_input("Vas a venir a mi fiesta de cumpleaños?")

pregunta=raw_input("Vas a venir?")
while pregunta!='Si':
    print "Vas a venir a mi nueva fiesta de cumpleaños?"
    pregunta=raw_input () #los parentesis son importantes conio

#while consta de tres partes:
    #- La variable
    #- La condición que se le establece
    #- Lo que hace hasta que esa condición se cumpla
print "dime n"
n=input()
print n

n=input("dime n")
print n
