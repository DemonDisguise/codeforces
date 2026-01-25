n: int = int(input())
for i in range(n):
    s: str = input()
    print(s if len(s) <= 10 else s[0] + str(len(s) - 2) + s[-1])