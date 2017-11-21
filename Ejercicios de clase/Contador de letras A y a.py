def contador_aes():
    palabra=raw_input("Dime una palabra:")
    suma=0
    suma2=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=='A':
            suma=suma + 1
        if palabra[cont]=='a':
            suma2=suma + 1
    print "En la palabra hay",suma,"letras A"
    print "En la palabra hay",suma2,"letras a"
contador_aes()
