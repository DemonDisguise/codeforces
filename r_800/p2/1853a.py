for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 10**18
    ok = True
    
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ok = False
            break
        ans = min(ans, (a[i + 1] - a[i]) // 2 + 1)
    
    print(0 if not ok else ans)
