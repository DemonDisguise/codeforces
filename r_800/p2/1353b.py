for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(sorted(map(int, input().split())))
    b = list(sorted(map(int, input().split()), reverse=True))
    
    for i in range(min(n, k)):
        if b[i] > a[i]:
            a[i] = b[i]
        else:
            break

    print(sum(a))