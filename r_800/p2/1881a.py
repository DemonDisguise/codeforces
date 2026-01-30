for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    res = 0
    for _ in range(6):
        if s in x:
            print(res)
            break
        x += x
        res += 1
    else:
        print(-1)
