for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mx = 0
    curr = 0
    for i in a:
        if i == 1:
            curr = 0
        else:
            curr += 1
            mx = max(mx, curr)
    print(mx)
