for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    count = 0 
    count += (b > a)
    count += (c > a)
    count += (d > a)

    print(count)
    