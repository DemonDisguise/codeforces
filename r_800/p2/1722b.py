for _ in range(int(input())):
    n = int(input())
    r1 = input().replace('G', 'B')
    r2 = input().replace('G', 'B')
    print("YES" if r1 == r2 else "NO")
