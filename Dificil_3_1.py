lista=[2,3,5,7,11,13,17]
x=18
while (len(lista)<10002):
    if((2**(x-1))%x == 1):
        if((3**(x-1))%x == 1):
            if((5**(x-1))%x == 1):
                if((7**(x-1))%x == 1):
                    if((11**(x-1))%x == 1):
                         if((13**(x-1))%x == 1):
                              if((17**(x-1))%x == 1):
                                    lista.append(x)

    x = x+1

print(len(lista))
print(lista[-1])
