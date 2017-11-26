#Este programa calcula la letra del DNI español introduciendo un numero de 8 cifras#
def letra_DNI():
    dni=0
    letra = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    while dni<10000000:
        dni=input("Introduce un DNI(8 cifras): ")
        if dni<10000000:
            print "\n Este DNI no es valido. Escriba otro \n\n"
        letradni=dni%23
    print "La letra de su D.N.I.(",dni,") es la",letra[letradni]
    print "Para su registro, su D.N.I. es: ",dni,"-",letra[letradni]
letra_DNI()
    
