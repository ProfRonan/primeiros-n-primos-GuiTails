print("Quantos primos?")
F = int(input("> "))
O = F
N = 2
i = 1
Lista = []
if F <=0:
    print("Insira um número maior")
if F > 0:
    while True:
        i = i + 1
        if N % i !=0:
            i = i + 1
        if N % i ==0 and i !=N:
            N = N + 1
            i = 1
        if N % i ==0 and i ==N:
            F = F - 1
            i = 1
            Lista.append(N)
            if F > 0:
                N = N + 1
            if F <=0:
                F = O
                print((F),Lista)
                break
