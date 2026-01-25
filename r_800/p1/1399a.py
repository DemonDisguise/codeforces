for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split())) 
    a.sort()

    p = True
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            p = False
            break
    
    print("YES" if p else "NO")
    