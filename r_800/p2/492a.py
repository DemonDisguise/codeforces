n = int(input())

used = 0
need = 0 
h = 0

while used + need + h + 1 <= n:
    h += 1
    need += h
    used += need

print(h)
