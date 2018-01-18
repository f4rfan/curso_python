def nombres():
    n = int(input("Cantidad de nombres a introducir: "))
    noms = []
    for i in range(n):
        noms.append(input("Nombre "+str(i)+': '))
    letra = input("Letra a buscar: ")
    letra = letra.lower()[0]
    encontrados = []
    for i in noms:
        if i.lower()[0]==letra:
            encontrados.append(i)
        else:
            print('No se encontraron coincidencias')
    for i in encontrados:
            print(i)
    input()

nombres()
