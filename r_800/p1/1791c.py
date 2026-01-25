for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    j = n - 1
    
    while i < j and s[i] != s[j]:
        i += 1
        j -= 1
    
    print(j - i + 1)
