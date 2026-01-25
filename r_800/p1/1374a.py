for _ in range(int(input())):
    x, y, n = map(int, input().split())

    if y > n:
        print(-1)
    else:
        c = (n - y) // x
        print((x * c) + y)
