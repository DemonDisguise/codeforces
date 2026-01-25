n = int(input())
grps = 1
prev = input()

for _ in range(n - 1):
    curr = input()
    if curr != prev:
        grps += 1
    prev = curr
print(grps)