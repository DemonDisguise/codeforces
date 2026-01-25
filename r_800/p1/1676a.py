t = int(input())

for _ in range(t):
    s = input()

    print("YES" if sum(map(int, s[:3])) == sum(map(int, s[3:])) else "NO")
