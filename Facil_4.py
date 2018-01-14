def generar_n_caracteres(n,c):
    print(n*c)
    for i in range(n):
        print(c, end='')
    input()

c = input("Caracter elegido: ")
n = int(input("Cantidad de caracteres deseados: "))

generar_n_caracteres(n,c)
