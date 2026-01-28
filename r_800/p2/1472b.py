for _ in range(int(input())):
    n = int(input())
    cnt1 = 0
    cnt2 = 0

    for x in map(int, input().split()):
        if x == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    total = cnt1 + 2 * cnt2

    if total % 2 != 0:
        print("NO")
    else:
        half = total // 2
        if half % 2 == 0 or (half % 2 == 1 and cnt1 != 0):
            print("YES")
        else:
            print("NO")