for _ in range(int(input())):
    n = int(input())
    s = input()

    seen = set()
    seen.add(s[0])        
    ok = True
    
    for i in range(1, n):
        if s[i] != s[i - 1]:
            if s[i] in seen:
                ok = False
                break
            seen.add(s[i])
    
    print("YES" if ok else "NO")
