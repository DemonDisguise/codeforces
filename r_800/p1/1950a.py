for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print(
        "STAIR" if a < b < c else
        "PEAK" if a < b > c else
        "NONE"
    )