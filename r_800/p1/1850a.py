for _ in range(int(input())):
    a = list(map(int, input().split()))

    if sum(a) - min(a) >= 10:
        print("YES")
    else:
        print("NO")
