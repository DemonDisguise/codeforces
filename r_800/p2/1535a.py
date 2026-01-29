for _ in range(int(input())):
    s1, s2, s3, s4 = map(int, input().split())

    l1, r1 = min(s1, s2), max(s1, s2)
    l2, r2 = min(s3, s4), max(s3, s4)
    print("YES" if max(l1, l2) <= min(r1, r2) else "NO")
