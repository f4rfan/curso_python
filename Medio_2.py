fibonacci = []
k = int(input("Cantidad de numeros a calcular: "))

for i in range(k):
    if i < 2:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

print('Se crearon ',len(fibonacci),' elementos!!\n','Tu secuencia es:\n',fibonacci[::1],sep='')

input("Presiona enter para terminar")
