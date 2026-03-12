for _ in range(int(input())):
    mx = -1001
    mn = 1001
    
    for _ in range(4):
        x = int(input().split()[0])
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    
    size = mx - mn
    print(size * size)    
    