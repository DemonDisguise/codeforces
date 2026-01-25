n = int(input())
x = list(map(int, input().split()))

ans = 0
max =  x[0]
min = x[0]

for i in range(1, n):
    if x[i] > max:
        ans += 1
        max = x[i]
    elif x[i] < min:
        ans += 1
        min = x[i]

print(ans)