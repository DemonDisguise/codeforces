import math

for _ in range(int(input())):
    n = int(input())
    a = sum(map(int, input().split()))
    
    r = math.isqrt(a)
    print("YES" if r * r == a else "NO")
    