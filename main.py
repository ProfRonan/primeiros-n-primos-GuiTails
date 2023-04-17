print("Quantos primos?")
F = int(input("> "))
N = 2
i = 1
if F <=0:
    print("Insira um número maior")
if F > 0:
    while True:
        i = i + 1
        if N % i ==0 and i !=N:
            N = N + 1
        if N % i ==0 and i ==N:
            F = F - 1
            i = 1
            if F > 0:
                print(N)
                N = N + 1
            if F <=0:
                print(N)
                break
