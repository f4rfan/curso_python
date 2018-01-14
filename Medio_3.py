def nombres():
    n = int(input("Cantidad de nombres a introducir: "))
    noms = []
    for i in range(n):
        noms.append(input("Nombre "+str(i)+': '))
    letra = input("Letra a buscar: ")
    encontrados = []
    for i in noms:
        if i.lower()[0]==letra.lower()[0]:
            encontrados.append(i)
    for i in encontrados:
            print(i)
    input()

nombres()
