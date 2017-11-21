def contador_vocales():
    palabra=raw_input("Dime una palabra:")
    A=0
    E=0
    I=0
    O=0
    U=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=='A' or palabra[cont]=='a':
            A=A + 1
        if palabra[cont]=='E' or palabra[cont]=='e':
            E=E + 1
        if palabra[cont]=='I'or palabra[cont]=='i':
            I=I + 1
        if palabra[cont]=='O' or palabra[cont]=='o':
            O=O + 1
        if palabra[cont]=='U' or palabra[cont]=='u':
            U=U + 1
    print "En la palabra hay",A,"letras A"
    print "En la palabra hay",E,"letras E"
    print "En la palabra hay",I,"letras I"
    print "En la palabra hay",O,"letras O"
    print "En la palabra hay",U,"letras U"
contador_vocales()
