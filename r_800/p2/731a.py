s = input().strip()

cur = 'a'
ans = 0

for ch in s:
    d = abs(ord(ch) - ord(cur))
    ans += min(d, 26 - d)
    cur = ch

print(ans)
