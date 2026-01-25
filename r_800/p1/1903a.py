for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if a == sorted(a) or k >= 2:
        print("YES")
    else:
        print("NO")
        