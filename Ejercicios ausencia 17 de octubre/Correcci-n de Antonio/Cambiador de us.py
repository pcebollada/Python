def pig_latin():
    texto=raw_input("Escribe un texto extenso: ")
    for cont in range(0,len(texto),1):
        if texto[cont]=='A' or texto[cont]=='a'or texto[cont]=='E' or texto[cont]=='e' or texto[cont]=='I'or texto[cont]=='i'or texto[cont]=='O'or texto[cont]=='o':
            print 'u',
        else:
            print texto[cont],
pig_latin()
#El diagrama de flujo seria un inicio, un trapecio para el raw_input, un hexágono para el "for cont", del cual sale un cuadrado con un sí y un no
            
