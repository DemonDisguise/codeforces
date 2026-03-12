for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total_twos = a.count(2)

    if total_twos % 2 == 1:
        print(-1)
        continue

    need = total_twos // 2
    cnt = 0

    for i in range(n):
        if a[i] == 2:
            cnt += 1
        if cnt == need:
            print(i + 1)   
            break
