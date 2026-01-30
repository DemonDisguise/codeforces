for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    need = 3 * max(a, b, c) - (a + b + c)
    print("YES" if n >= need and (n - need) % 3 == 0 else "NO")
