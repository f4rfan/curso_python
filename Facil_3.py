def longitud_cadena():
    cadena = input("Dame la cadena a analizar: ")
    longitud = 0
    for i in cadena:
        longitud += 1
    print(longitud)
    input()

def longitud_lista():
    lista = []
    longitud = 0
    lista.append(input("Anadir elemento a la lista: "))
    a = int(input("Desea anadir mas elementos a la lista ?\n1.- Si   2.- No\n"))
    if a==1:
        res = True
    else:
        res = False
    while res:
        lista.append(input("Anadir elemento a la lista: "))
        a = input("Desea anadir mas elementos a la lista ?\n1.- Si   2.- No\n")
        if a==1:
            res = True
        else:
            res = False
    for i in lista:
        longitud += 1
    print(longitud)
    input()

longitud_cadena()
longitud_lista()
