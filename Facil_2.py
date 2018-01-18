def max_de_tres():
    a = input("Dame el primer numero: ")
    b = input("Dame el segundo numero: ")
    c = input("Dame el tercer numero: ")
    if a>b:
        if a>c:
            print('Entre los numeros introducidos, el mas grande es el primero,',a)
        else:
            print('Entre los numeros introducidos, el mas grande es el tercero,',c)
    else:
        if b>c:
            print('Entre los numeros introducidos, el mas grande es el segundo,',b)
        else:
            print('Entre los numeros introducidos, el mas grande es el tercero,',c)
    input()


max_de_tres()
