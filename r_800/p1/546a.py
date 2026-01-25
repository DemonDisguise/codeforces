k, n, w = map(int, input().split())

borrow = (k * ((w * (w + 1))//2)) - n

print(borrow if borrow > 0 else 0)
