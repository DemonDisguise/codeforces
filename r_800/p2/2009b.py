for _ in range(int(input())):
    n = int(input())
    a = [0] * n
    for i in range(n - 1, -1, -1):
        s = input()
        a[i] = s.index('#') + 1
    print(*a)
