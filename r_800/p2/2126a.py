def solve():
    for _ in range(int(input())):
        x = int(input())
        best = 9
        while x:
            d = x % 10
            if d < best:
                best = d
                if best == 0:
                    break
            x //= 10
        print(best)

if __name__ == "__main__":
    solve()