for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = min(b, 2 * a)
    print((n // 2) * s + (n % 2) * a)
