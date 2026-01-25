n = int(input())
s = input().lower()

print("YES" if len({c for c in s if c.isalpha()}) == 26 else "NO")
