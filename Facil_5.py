def inversa():
    cadena = input("Dame la cadena a invertir: ")
    cont = -1
    inversion = ""
    for i in cadena:
        inversion = inversion + cadena[cont]
        cont -= 1
    print(inversion)
    input()

inversa()
