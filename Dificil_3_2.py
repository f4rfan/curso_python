lista=[2,3,5,7,11,13,17]
x=18
while (len(lista)<10002):
    comp=0
    for z in range(len(lista)):
        if(pow(lista[z], x-1, x) == 1):
            comp+=1

    if(comp==len(lista)):
        lista.append(x)

    x = x+1

print(len(lista))
print(lista[-1])
