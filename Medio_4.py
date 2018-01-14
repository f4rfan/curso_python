def contar_vocales():
    cadena = input("Cadena a analizar: ")
    cantidades = [0,0,0,0,0]
    for i in cadena.lower():
        if i=='a':
            cantidades[0]+=1
        elif i=='e':
            cantidades[1]+=1
        elif i=='i':
            cantidades[2]+=1
        elif i=='o':
            cantidades[3]+=1
        elif i=='u':
            cantidades[4]+=1
    vocales = ["a","e","i","o","u"]
    print("La cadena contiene: ")
    for i in range(5):
        print(vocales[i],cantidades[i])
    input()

contar_vocales()
    
