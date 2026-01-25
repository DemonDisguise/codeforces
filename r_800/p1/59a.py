s = input()

upper = sum(c.isupper() for c in s)
print(s.upper() if upper > len(s) - upper else s.lower())
