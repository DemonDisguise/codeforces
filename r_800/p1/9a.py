from math import gcd

y, w = map(int, input().split())

m = max(y, w)
fav = 6 - m + 1
g = gcd(fav, 6)

print(f"{fav//g}/{6//g}")
