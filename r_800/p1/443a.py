s = input().strip()[1:-1]
print(len(set(s.split(", "))) if s else 0)
