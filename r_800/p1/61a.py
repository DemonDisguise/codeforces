x = input()
y = input()

res = []
for i in range(len(x)):
    res.append('0' if x[i] == y[i] else '1')
print(''.join(res))        