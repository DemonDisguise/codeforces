for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    w_even = 0
    w_odd = 0
    
    for i in range(n):
        if i & 1 == 0 and a[i] & 1 != 0:
            w_even += 1
        elif i & 1 == 1 and a[i] & 1 != 1:
            w_odd += 1
    
    if w_even != w_odd:
        print(-1)
    else:
        print(w_even)
        