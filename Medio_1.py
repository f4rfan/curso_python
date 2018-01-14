def vocales():
    cadena = input("Dame la cadena a analizar: ")
    vocal = ['a','e','i','o','u','A','E','I','O','U']
    resultado = []
    for i in cadena:
        if i in vocal:
            if i not in resultado:
                resultado.append(i)

    for i in resultado:
        print(i)

vocales()
