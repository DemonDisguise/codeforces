for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split())) + [x]

    mx = 0
    
    for i in range(1, len(a)):
        gap = a[i] - a[i - 1]
        if i == len(a) - 1:
            gap *= 2
        mx = max(mx, gap)
    
    print(mx)
