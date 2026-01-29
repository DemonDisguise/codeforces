for _ in range(int(input())):
    n = int(input())
    x = n // 3
    if n % 3 == 0:
        print(x, x)
    elif n % 3 == 1:
        print(x + 1, x)
    else:
        print(x, x + 1)
