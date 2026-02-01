for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    odd = sum(x & 1 for x in a)
    print("YES" if odd == n else "NO")
