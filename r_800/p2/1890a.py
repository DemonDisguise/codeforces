from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = Counter(a)
    vals = sorted(freq.values())
    
    if len(vals) == 1:
        print("YES")
    elif len(vals) == 2 and vals[0] == n // 2 and vals[1] == (n + 1) // 2:
        print("YES")
    else:
        print("NO")
