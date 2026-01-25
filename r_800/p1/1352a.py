t = int(input())

for _ in range(t):
    n = int(input())
    k = 0
    if n < 10:
        k = 1
        print(k)
        print(n)
    else:
        l = 0
        res = []
        while n > 0:
            if n % 10 != 0:
                k += 1
                res.append((n % 10) * (10 ** l))
            l += 1
            n //= 10
        print(k)
        print(*res)
            