n: int = int(input())
x: int = 0

for _ in range(n):
    ops: str = input()
    x += 1 if '++' in ops else -1
print(x)