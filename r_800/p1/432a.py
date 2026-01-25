n, k = map(int, input().split())
y = list(map(int, input().split()))

print(sum(1 for i in y if i + k <= 5) // 3)
