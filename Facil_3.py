def longitud_cadena():
    cadena = input("Dame la cadena a analizar: ")
    longitud = 0
    for i in cadena:
        longitud += 1
    print('La cadena tiene una longitud de',longitud,'caracteres.')
    input()

def longitud_lista():
    lista = []
    lista.append(input("Elemento a anadir a la lista: "))
    a = int(input("Desea anadir mas elementos a la lista ?\n1.- Si   2.- No\n"))
    if a==1:
        res = True
    else:
        res = False
    while res:
        lista.append(input("Elemento a anadir a la lista: "))
        a = input("Desea anadir mas elementos a la lista ?\n1.- Si   2.- No\n")
        if a==1:
            res = True
        else:
            res = False

    longitud = 0
    for i in lista:
        longitud += 1
    print('La lista de elementos creados cuenta con',longitud,'elemento(s).')
    input()

respuesta = 1
while respuesta:
    respuesta = int(input('De que deseas calcular la longitud:\n1)Cadena de caracteres\n2)Lista de elementos(se creara una lista y se anadiran elementos a ella)\n3)Salir\nRespuesta:'))
    if respuesta == 1:
        longitud_cadena()
    elif respuesta == 2:
        longitud_lista()
    else:
        break
