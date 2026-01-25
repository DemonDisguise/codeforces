from collections import Counter

n = int(input())
t = list(map(int, input().split()))

cntr = {1: [], 2: [], 3: []}
for i in range(n):
    cntr[t[i]].append(i + 1)
    

k = min(len(i) for i in cntr.values())
print(k)

for i in range(k):
    print(cntr[1][i], cntr[2][i], cntr[3][i])


