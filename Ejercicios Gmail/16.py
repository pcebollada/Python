#Escriba un programa que lea dos horas distintas, expresadas como horas,
#minutos y segundos, ycompruebe si la segunda es posterior a la primera.
def comparador_horas():
    a=input("Dime un número de horas para la primera hora: ")
    b=input("Dime un número de minutos para la primera hora: ")
    c=input("Dime un número de segundos para la primera hora: ")
    print "La hora escrita es:",a,"horas",b,"minutos y ",c,"segundos"
    d=input("Dime un número de horas para la segunda hora: ")
    e=input("Dime un número de minutos para la primera hora: ")
    f=input("Dime un número de segundos para la primera hora: ")
    print "La hora escrita es:",d,"horas",e,"minutos y ",f,"segundos"

    if a>d:
        print "La primera hora es mayor"
    if a<d:
        print "La segunda hora es mayor"
    if a==d:
        if b>e:
            print "La primera hora es mayor"
        if b<e:
            print "La segunda hora es mayor"
        if b==e:
            if c>f:
                print "La primera hora es mayor"
            if c<f:
                print "La segunda hora es mayor"
            if c==f:
                print "Las horas son iguales"
comparador_horas()
            
        
