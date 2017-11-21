def calculador():
    h=input("Dime un numero de horas: ")
    m=input("Dime un numero de minutos: ")
    s=input("Dime un numero de segundos: ")
    print "La hora escrita es",h,":",m,":",s
    horatotal=h*3600+m*60+s
    horatotal=horatotal+1
    hfinal=horatotal/3600
    mfinal=(horatotal-hfinal*3600)/60
    sfinal=(horatotal-hfinal*3600)%60
    print "La hora final es",hfinal,":",mfinal,":",sfinal
calculador()
