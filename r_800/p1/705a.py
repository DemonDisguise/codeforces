n = int(input())
x = False
res = []
for i in range(n):
    res.append(f"I {'hate' if i % 2 == 0 else "love"} {'that' if i < n - 1 else 'it'}")

print(" ".join(res))