n, h = map(int, input().split())

a = list(map(int, input().split()))

res = 0
for i in a:
    res += 2 if i > h else 1

print(res)