n = int(input())
a = list(map(int, input().split()))

max_h = max(a)
min_h = min(a)

max_idx = a.index(max_h)
min_idx = n - 1 - a[::-1].index(min_h)

ans = max_idx + (n - 1 - min_idx)

if max_idx > min_idx:
    ans -= 1

print(ans)
