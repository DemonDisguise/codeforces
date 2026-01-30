n, m = map(int, input().split())
color = False

for _ in range(n):
    s = input()
    if not color and any(ch in s for ch in "CMY"):
        color = True

print("#Color" if color else "#Black&White")
