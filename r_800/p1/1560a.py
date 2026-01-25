good = []
x = 1
while len(good) < 1000:
    if x % 3 != 0 and x % 10 != 3:
        good.append(x)
    x += 1

for _ in range(int(input())):
    k = int(input())
    print(good[k - 1])
    