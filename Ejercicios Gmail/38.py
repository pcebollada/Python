def numero():
    valor=1

    while valor<2048:
        if valor%10>=0 and valor%10<=5:
            print valor
        valor=valor*2
numero()
