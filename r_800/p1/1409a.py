for _ in range(int(input())):
    a, b = map(int, input().split())
    d = abs(a - b)
    moves = d // 10
    if d % 10 != 0:
        moves += 1
    print(moves)