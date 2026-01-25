target = set("Timur")

for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if n == 5 and set(s) == target else "NO")
    