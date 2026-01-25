n, k = map(int, input().split())
t = (4 * 60) - k 
s = 0
ans = 0

for i in range(1, n + 1):
    s += 5 * i
    
    if s > t:
        break
    
    ans += 1

print(ans)
