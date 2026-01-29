n = int(input())

if n % 2 == 0:
    print(n // 2)
    print(" ".join(["2"] * (n // 2)))
else:
    print((n - 3) // 2 + 1)
    print("3", " ".join(["2"] * ((n - 3) // 2)))
