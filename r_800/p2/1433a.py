for _ in range(int(input())):
    x = input().strip()
    d = int(x[0])
    n = len(x)

    print(10 * (d - 1) + (n * (n + 1)) // 2)
        