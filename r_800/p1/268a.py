n = int(input())
uni = []
for _ in range(n):
    uni.append(tuple(map(int, input().split())))
res = 0
away_count = {}

for home, away in uni:
    away_count[away] = away_count.get(away, 0) + 1
    
for i in range(n):
    res += away_count.get(uni[i][0], 0)

print(res)
