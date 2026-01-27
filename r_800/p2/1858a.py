for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print("First" if a > b or (c % 2 == 1 and a == b) else "Second")

