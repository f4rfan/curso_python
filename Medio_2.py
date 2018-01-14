fibonacci = []
k = int(input("Cuantos numeros deseas calcular ? \n"))

for i in range(k):
    if i == 0:
        fibonacci.append(1)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

print('Tu secuencia es: '+ str(fibonacci[::1]))

input("Presiona enter para terminar")
