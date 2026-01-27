for _ in range(int(input())):
    s = input()
    n = len(s) // 2
    print("YES" if s[:n] == s[n:] else "NO")
