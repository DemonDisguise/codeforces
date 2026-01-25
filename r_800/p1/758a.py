n = int(input())
a = list(map(int, input().split()))
mx = max(a)
print(mx * n - sum(a))
