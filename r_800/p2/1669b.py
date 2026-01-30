for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = -1
    for i in range(n - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            ans = a[i]
            break
    
    print(ans)
