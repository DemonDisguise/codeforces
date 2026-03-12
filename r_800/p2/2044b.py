t = int(input())
for _ in range(t):
    s = input().strip()
    s = s[::-1]  

    res = []
    for c in s:
        if c == 'p':
            res.append('q')
        elif c == 'q':
            res.append('p')
        else:
            res.append(c)  

    print(''.join(res))
