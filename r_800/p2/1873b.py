for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    prod = 1
    used = False
    mn = min(a)

    for i in a:
        if i == mn and not used:
            prod *= (i + 1)
            used = True
        else:
            prod *= i
    
    print(prod)
