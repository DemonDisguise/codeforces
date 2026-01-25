a, b = map(int, input().split())
yrs = 0

while a <= b:
    a *= 3
    b *= 2
    yrs += 1

print(yrs)