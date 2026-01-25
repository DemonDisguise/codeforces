n: int = int(input())
max_solved = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        max_solved += 1

print(max_solved)