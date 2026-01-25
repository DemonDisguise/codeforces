m, n = map(int, input().split())

rf = '#' * n
rl = '#' + '.' * (n - 1)
rr = '.' * (n - 1) + '#'

for i in range(1, m + 1):
    if i % 2 != 0:
        print(rf)
    elif i % 4 == 0:
        print(rl)
    else:
        print(rr)
    