n = int(input())
res = 0
ans = 0

x = list(map(int, input().split()))
for i in x:
    if i != -1:
        res += i
    else:
        if res > 0:
            res -= 1
        else:
            ans += 1

print(ans)
