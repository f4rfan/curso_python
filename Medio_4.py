def contar_vocales():
    cadena = input("Cadena a analizar: ")
    cantidades = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in cadena.lower():
        if i=='a':
            cantidades['a']+=1
        elif i=='e':
            cantidades['e']+=1
        elif i=='i':
            cantidades['i']+=1
        elif i=='o':
            cantidades['o']+=1
        elif i=='u':
            cantidades['u']+=1
    print("La cadena contiene: ")
    for i in cantidades:
        print(i,'=',cantidades[i])
    input()

contar_vocales()
