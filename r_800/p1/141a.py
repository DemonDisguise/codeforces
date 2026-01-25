from collections import Counter

a = input()
b = input()
c = input()

print("YES" if Counter(a + b) == Counter(c) else "NO")
