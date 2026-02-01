for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    mn = a[0]
    cnt = a.count(mn)
    
    if cnt == n:
        print(-1)
    else:
        print(cnt, n - cnt)
        print(*a[:cnt])
        print(*a[cnt:])
