t = "codeforces"

for _ in range(int(input())):
    s = input()
    print(sum(a != b for a, b in zip(s, t)))
