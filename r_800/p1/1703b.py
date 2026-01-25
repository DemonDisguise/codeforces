for _ in range(int(input())):
    n = int(input())
    s = input()
    seen = set()
    res = 0
    for c in s:
        if c not in seen:
            res += 2
            seen.add(c)
        else:
            res += 1
            
    print(res)  
