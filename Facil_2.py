def max_de_tres():
    a = input("Dame el primer numero: ")
    b = input("Dame el segundo numero: ")
    c = input("Dame el tercer numero: ")
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)
    input()


max_de_tres()
