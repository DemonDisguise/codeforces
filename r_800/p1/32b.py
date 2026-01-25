s = input()
i = 0
res = []

while i < len(s):
    if s[i] == '.':
        res.append('0')
        i += 1
    else:
        res.append('1' if s[i+1] == '.' else '2')
        i += 2

print(''.join(res))
