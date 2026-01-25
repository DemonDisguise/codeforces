n, k = map(int, input().split())
scores = list(map(int, input().split()))
res = 0

for i in scores:
    if i >= scores[k - 1] and i > 0:
        res += 1

print(res)