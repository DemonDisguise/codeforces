n, k, l, c, d, p, nl, np = map(int, input().split())

print(min(c * d, ((k * l)// nl), (p // np)) // n)
