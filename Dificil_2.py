serie = []

for x in range(100,1000):
    for y in range(100,1000):
        valores =[]
        if (x*y) < 1000000 and (x*y) >= 100000:
            valor = str(x*y)
            if valor[:3] == valor[-1:-4:-1]:
                if (x*y) not in serie:
                    valores = [x*y,x,y]
                    serie.append(valores)

serie.sort()

for i in serie:
    print(i)
