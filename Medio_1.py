def vocales():
    cadena = input("Dame la cadena a analizar: ")
    vocal = ['a','e','i','o','u']
    resultado = []
    for i in cadena.lower():
        if i in vocal:
            if i not in resultado:
                resultado.append(i)

    for i in resultado:
        print(i)

vocales()
